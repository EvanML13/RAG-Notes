# RAG System Overview
**Retrieval Augmented Generation (RAG) System**: An AI framework that boosts Large Language Models by connecting them to external authoritative knowledge bases to fetch relevant information before generating answers, making responses more accurate and specific.  

**Embedding**: Numeric representations of data like text, images, or audio that the machine can process.  

**Vector Database**: Stores, manages, and searches embeddings. 

**Optical Character Recognition (OCR)**: A system that converts images of text (typed, handwritten, or printed)  from documents or photos into machine-readable, editable, and searchable text.   

**Semantic Chunking**: Splits text into meaningful, context-rich segments based on topic shifts by analyzing sentence meaning with vector embeddings.     

1. Convert Notes into Text
2. Turn the Text into Embeddings
3. Store the Embeddings in a Vector Database  
4. When a Question is Asked to the System...
  i. Embed the question
  ii. Retrieve the most relevant note chunks
  iii. Feed those  chunks into the LLM as context
  iv. Get a grounded answer

iPad Notes/PDFs/Slides  
↓  
Text Extraction (OCR + Parsing)  
↓  
Chunking (Small Semantic Pieces)  
↓  
Embedding Model   
↓  
Vector Database   
↓  
User Question  
↓  
Question Embedding   
↓  
Similarity Search  
↓  
Chunking (Small Semantic Pieces)  
↓  
LLM Answer (With Citation)  

git clone HTTPS Repositority URL

OCR: PaddleOCR

Activate Virtual Environment: source venv/bin/activate

- January 4th 2026
- Evan Leonard 
