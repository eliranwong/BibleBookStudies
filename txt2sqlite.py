import os, re, markdown2, sqlite3
from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
from agentmake import readTextFile

DATABASE_NAME = 'ai_book_analysis.db'

def initialize_db(db_name=DATABASE_NAME):
    """
    Connects to the SQLite database and creates the 'Introduction' table 
    if it does not already exist.
    """
    try:
        # Connect to the SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # SQL command to create the table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Introduction (
            Book INTEGER,
            Section INTEGER,
            Content TEXT
        );
        """
        
        # Execute the table creation command
        cursor.execute(create_table_sql)
        conn.commit()
        
        print(f"Database '{db_name}' initialized successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"An error occurred during database initialization: {e}")
        return None


def insert_section(conn, book, section, content, update=False):
    """
    Inserts a new entry into the Introduction table.
    
    Args:
        conn (sqlite3.Connection): The database connection object.
        book (int): The book number.
        section (int): The chapter number.
        content (str): The text of the Introduction.
    """
    if conn is None:
        print("Cannot insert data: Database connection is not established.")
        return

    try:
        cursor = conn.cursor()
        if update:
            update_query = """
                UPDATE Introduction 
                SET Content = ? 
                WHERE Book = ? AND Section = ?
            """
            cursor.execute(update_query, (content, book, section))
        else:
            insert_sql = """
            INSERT INTO Introduction (Book, Section, Content)
            VALUES (?, ?, ?);
            """
            cursor.execute(insert_sql, (book, section, content))
        conn.commit()
        print(f"{'Updated' if update else 'Inserted'}: Book={book}, Section={section}")
        
    except sqlite3.Error as e:
        print(f"An error occurred during insertion: {e}")

def get_contents(b, lang="eng"):
    parser = BibleVerseParser(False, language=lang)
    def process_content(parser, content):
        # parse content
        content = re.sub("》([0-9]+?:[0-9-]+?)([^0-9-])", r" \1》\2", content)
        content = re.sub("([^0-9 ])([0-9]+?:)", r"\1 \2", content)
        content = parser.parseText(content)
        # convert md to html
        content = markdown2.markdown(content, extras=["tables","fenced-code-blocks","toc","codelite"])
        content = content.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
        # convert links
        content = re.sub(r'''(onclick|ondblclick)="(bcv)\((.*?)\)"''', r'''\1="emitEvent('\2', [\3]); return false;"''', content)
        return content
    contents = []
    conversation_file = os.path.join(lang, f"{b}.py")
    if os.path.isfile(conversation_file):
        contents = [process_content(parser, i["content"]) for i in eval(readTextFile(conversation_file)) if i.get("role", "") == "assistant" and not i.get("content", "") == "Sure! Let's dive into the analysis process."]
    return contents

if __name__ == '__main__':
    # 1. Initialize the database and get the connection object
    if db_connection := initialize_db():
        for i in range(1, 67):
            for ii, content in enumerate(get_contents(i, lang="eng")):
                insert_section(db_connection, i, ii, content)
        db_connection.close()