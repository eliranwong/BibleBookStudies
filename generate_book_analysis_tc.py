from agentmake import agentmake, writeTextFile
from agentmake.plugins.uba.lib.BibleBooks import BibleBooks
import pprint, os

def request_chinese_response(prompt: str) -> str:
    return prompt + "\n\n# Response Language\n\nTraditional Chinese 繁體中文\n\n请使用繁體中文作所有回應，除了引用工具名稱或希伯來語或希臘語，或我特别要求你使用英文除外。"

AGENTMAKE_CONFIG = {
    "backend": "googleai",
    "stream": True,
    "print_on_terminal": True,
    "word_wrap": False,
}

LANGUAGE = "tc"
OT_BOOKS = [BibleBooks.abbrev["eng"][str(i)][-1] for i in range(1,40)]
NT_BOOKS = [BibleBooks.abbrev["eng"][str(i)][-1] for i in range(40,67)]
FINAL_INSTRUCTION = """# Instruction
Please provide me with the final answer to my original request based on the work that has been completed.

# Original Request
Perform a comprehensive analysis of the book of {book} in the Bible."""

# OT Book Analysis
queries = {
    'bible/introduce_book': "Write a detailed introduction on the book of {book}.",
    'bible/outline': "Provide a detailed outline of the book of {book}.",
    'bible/flow': "Analyze the thought progression of the book of {book}.",
    'bible/ot_context': "Detail the historical context of the book of {book}, including its Ancient Near Eastern (ANE) background and archaeological significance.",
    'bible/ot_themes': "Explore recurring motifs and primary messages in the book of {book}.",
    'bible/keywords': "Identify Bible keywords from the book of {book}.",
    'bible/theology': "Summarize the theological messages conveyed in the book of {book}.",
    'bible/canon': "Explain the canonical context of the book of {book}, detailing how it fits into the wider Old Testament and its relationship to the New Testament.",
    'bible/application': "Provide detailed applications for the entire book of {book}.",
}
for index, book in enumerate(OT_BOOKS):
    print(f"Processing book {index+1}/{len(OT_BOOKS)}: {book}")

    conversation_file = f'{LANGUAGE}/{index+1}.py'
    if os.path.isfile(conversation_file):
        continue
    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides detailed information about the books of the Bible."},
        {"role": "user", "content": f"Perform a comprehensive analysis of the book of {book} in the Bible."+"\n\n# Response Language\n\nTraditional Chinese 繁體中文\n\n请使用繁體中文作所有回應，除了引用工具名稱或希伯來語或希臘語，或我特别要求你使用英文除外。"},
        {"role": "assistant", "content": "好的！讓我們深入分析這本書。"},
    ]
    for instruction, query in queries.items():
        print("Request:", query.format(book=book))
        messages = agentmake(messages, **{'instruction': instruction, 'follow_up_prompt': query.format(book=book), 'system': "auto"}, **AGENTMAKE_CONFIG)
    
    print("Request:", FINAL_INSTRUCTION.format(book=book))
    messages = agentmake(messages, **{'follow_up_prompt': FINAL_INSTRUCTION.format(book=book), 'system': "write_final_answer"}, **AGENTMAKE_CONFIG)

    writeTextFile(conversation_file, pprint.pformat(messages))

    print(f"Completed processing for the book of {book}.")

# NT Book Analysis
queries = {
    'bible/introduce_book': "Write a detailed introduction on the book of {book}.",
    'bible/outline': "Provide a detailed outline of the book of {book}.",
    'bible/flow': "Analyze the thought progression of the book of {book}.",
    'bible/nt_context': "Detail the Greco-Roman or Jewish cultural backdrop and specific situational triggers for the book of {book}.", #NT specific
    'bible/nt_themes': "Explore recurring motifs and primary messages in the book of {book}.", #NT specific
    'bible/keywords': "Identify Bible keywords from the book of {book}.",
    'bible/theology': "Summarize the theological messages conveyed in the book of {book}.",
    'bible/canon': "Explain the canonical context of the book of {book}, detailing how it fits into the wider New Testament and the fulfillment of the Old Testament.", #NT specific
    'bible/application': "Provide detailed applications for the entire book of {book}.",
}
for index, book in enumerate(NT_BOOKS):
    print(f"Processing book {index+1}/{len(NT_BOOKS)}: {book}")

    conversation_file = f'{LANGUAGE}/{index+40}.py'
    if os.path.isfile(conversation_file):
        continue
    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides detailed information about the books of the Bible."},
        {"role": "user", "content": f"Perform a comprehensive analysis of the book of {book} in the Bible."},
        {"role": "assistant", "content": "好的！讓我們深入分析這本書。"},
    ]
    for instruction, query in queries.items():
        print("Request:", query.format(book=book))
        messages = agentmake(messages, **{'instruction': instruction, 'follow_up_prompt': request_chinese_response(query.format(book=book)), 'system': "auto"}, **AGENTMAKE_CONFIG)
    
    print("Request:", FINAL_INSTRUCTION.format(book=book))
    messages = agentmake(messages, **{'follow_up_prompt': request_chinese_response(FINAL_INSTRUCTION.format(book=book)), 'system': "write_final_answer"}, **AGENTMAKE_CONFIG)

    writeTextFile(conversation_file, pprint.pformat(messages))

    print(f"Completed processing for the book of {book}.")