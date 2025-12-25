# BibleBookStudies

In-depth study of the 66 books in the Bible.

Generated with [AgentMake AI](https://github.com/eliranwong/agentmake) and Gemini 2.5 Flash

## How it works?

- **Overview:** The project automates a book-by-book analysis of the Bible by constructing prompt sequences and calling an LLM wrapper to generate structured conversation outputs for each book.
- **Main script:** `generate_book_analysis.py` builds OT and NT book lists (via `agentmake.plugins.uba.lib.BibleBooks`) and iterates each book to run analysis queries.
- **Prompt flow:** For each book the script seeds a messages array then runs queries: introduce, outline, flow, context (OT/NT-specific), themes, keywords, theology, canon, application, and finally requests a consolidated answer.
- **Agent calls:** The script uses `agentmake(...)` with `AGENTMAKE_CONFIG` to send prompts to the configured backend; streaming and terminal output are controlled there.
- **Output:** Conversations are saved with `writeTextFile` under the language folder (for example, `eng/1.py`, `eng/40.py`). Existing files are skipped to avoid re-running analyses.
- **Prerequisites:** Configure `agentmake` credentials/backend, ensure language folders (e.g., `eng/`) exist, and install required Python dependencies.
- **Quick run:** Execute `python generate_book_analysis.py` to generate analyses; edit the `queries` dict or `AGENTMAKE_CONFIG` to customize prompts or model behavior.

# Distribution Licence

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Bible Book Studies</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://www.bibletools.app" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/BibleBookStudies" rel="dct:source">https://github.com/eliranwong/BibleBookStudies</a>.<br />Permissions beyond the scope of this license may be available at <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible/contact/contactform.php" rel="cc:morePermissions">https://marvel.bible/contact/contactform.php</a>.

# Published at:

English version:

https://biblemate.gospelchurch.uk/?d=true&s=true&l=3&bbt=NET&tbt=NET&tool=Analysis&bb=1&bc=1&bv=1&lang=eng

Traditional Chinese:

https://biblemate.gospelchurch.uk/?d=true&s=true&l=3&bbt=NET&tbt=NET&tool=Analysis&bb=1&bc=1&bv=1&lang=tc

Simplified Chinese:

https://biblemate.gospelchurch.uk/?d=true&s=true&l=3&bbt=NET&tbt=NET&tool=Analysis&bb=1&bc=1&bv=1&lang=sc

# Related Projects

This resource is built for BibleMate AI:

https://github.com/eliranwong/biblemate

https://github.com/eliranwong/biblemategui

Analysis of Every Single Book in the Bible

https://github.com/eliranwong/BibleBookStudies

Summary of Every Single Chapter in the Bible

https://github.com/eliranwong/BibleChapterSummaries

Commentary of Every Single Verse in the Bible

https://github.com/eliranwong/AI_Commentary