# Python Program which prints matching skills only once. ---> (edited  april 3)
import os
import pdfplumber

def search_pdfs(root_dir, search_term):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.pdf'):
                # Initialize flag variable
                found_search_term = False
                with pdfplumber.open(os.path.join(root, file)) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if search_term.lower() in text.lower():
                            # Set flag to True if search term is found
                            found_search_term = True
                # Print file path if search term is found for the first time in the file
                if found_search_term:
                    print(f"Found '{search_term}' in {os.path.join(root, file)}")
user_input = input("Enter a SKILL to SEARCH : ")
search_pdfs('C:/Users/3iintr00203/Desktop/resumes/perfect resumes', user_input)