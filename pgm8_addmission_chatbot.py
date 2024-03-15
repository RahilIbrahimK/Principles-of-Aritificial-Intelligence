import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define intent patterns and corresponding responses
intent_patterns = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "farewell": ["goodbye", "bye", "see you later", "take care", "farewell", "have a good one"],
    "admission_inquiry": ["admission", "apply", "enroll", "admission process", "get into college"],
    "program_inquiry": ["program", "course", "degree"],
    "deadline_inquiry": ["deadline", "application deadline"],
    "financial_aid_inquiry": ["financial aid", "scholarship", "tuition fee"],
    "contact_inquiry": ["contact", "email", "phone", "contact information"],
    "help": ["help", "assist", "guide"],
    "course_inquiry": ["course", "class", "subject", "lecture", "study", "curriculum", "syllabus"],
    "schedule_inquiry": ["schedule", "timetable", "class timing", "session time", "course schedule", "class schedule"],
    "prerequisite_inquiry": ["prerequisite", "requirement", "eligibility", "qualification", "precondition", "prior knowledge"],
    "description_inquiry": ["description", "overview", "details", "information", "about", "what is"],
    "faculty_inquiry": ["faculty", "instructor", "professor", "teacher", "lecturer", "teaching staff"],
    "location_inquiry": ["location", "where", "venue", "campus", "address"],

}

intent_responses = {
    "greeting": "Hello! How can I assist you with your admission inquiry?",
    "farewell": "Goodbye! Feel free to reach out if you have any more questions.",
    "admission_inquiry": "For admission inquiries, please visit our website or contact the admission office.",
    "program_inquiry": "Our institution offers a variety of programs. Which program are you interested in?",
    "deadline_inquiry": "The admission deadline varies depending on the program. Please check our website for specific deadlines.",
    "financial_aid_inquiry": "Information about financial aid options is available on our website or you can contact the financial aid office for assistance.",
    "contact_inquiry": "You can contact our admission office at admission@example.com or call +123456789.",
    "help": "How can I assist you further?",
    "course_inquiry": "We offer a wide range of courses in various disciplines. Could you please specify which course you are interested in?",
"schedule_inquiry": "The class schedule varies depending on the course and semester. You can find the detailed schedule on our website or contact the registrar's office for more information.",
"prerequisite_inquiry": "The prerequisites for each course may vary. Please check the course description or contact the academic advisor for specific prerequisite requirements.",
"description_inquiry": "Each course has a detailed description outlining its content, objectives, and requirements. You can find this information in the course catalog or on our website.",
"faculty_inquiry": "Our courses are taught by experienced and qualified faculty members who are experts in their fields. You can find information about the faculty members on our website.",
"location_inquiry": "Our classes are held on campus at [campus name]. You can find the campus address and directions on our website or contact the campus office for assistance.",

}

# Define a function to classify intent based on user input
def classify_intent(user_input):
    doc = nlp(user_input)
    for intent, patterns in intent_patterns.items():
        for pattern in patterns:
            if pattern in user_input:
                return intent
    return None

# Define a function to interact with the chatbot
def admission_chat():
    print("Welcome to the Admission Chatbot. How can I assist you today?")
    print("Type 'quit' to exit.")

    # Start chatting
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        intent = classify_intent(user_input)
        if intent:
            print("Chatbot:", intent_responses[intent])
        else:
            print("Chatbot: I'm sorry, I didn't understand your query.")

if __name__ == "__main__":
    # Start the admission chat
    admission_chat()