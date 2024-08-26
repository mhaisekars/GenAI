from langchain_utils import LangchainWrapper
from create_db import DatabaseFactory

def main():
    #B_INST,E_INST="[INST]","[/INST]"
    db_instance = DatabaseFactory()
    db = db_instance.get_engine()
    wrapper = LangchainWrapper()
    wrapper.create_db_instance(db)
    wrapper.create_model()
    wrapper.create_chain()


    print(wrapper.get_response("How many passengers are above 20 years of age?"))

    while True:
        #wait for user input
        choice=input("Press Enter to exit...")
        if choice=="q":
            break
        #get new input question 
        question = input("Enter a new question: ")
        response = wrapper.get_response(question)
        print(response)


if __name__ == "__main__":
    main()