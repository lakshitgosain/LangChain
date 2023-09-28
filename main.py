from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrpae_linkedin_profile
from agents.linkedin_lookup_agent import  lookup as linkedin_lookup_agent

if __name__ == '__main__':
    print("Hello Langchain Lakshit THis side")

    linkedin_profile_url=linkedin_lookup_agent(name='Lakshit Gosain')
    print(linkedin_profile_url)

    # information="""
    #     Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$241 billion as of September 2023, according to the Bloomberg Billionaires Index, and $261 billion according to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.
    # """
    #
    # linkedin_data = scrpae_linkedin_profile("Dynamic")
    # print(linkedin_data)
    #
    # summary_template = """
    #     given the information {information} about a person from I want you to create:
    #     1. a short summary
    #     2. two interesting faces about them
    #     """
    # summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    # llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo') #temperateure means the language model wont be creative
    #
    # chain=LLMChain(llm=llm, prompt=summary_prompt_template)
    #
    # print(chain.run(information=linkedin_data))



