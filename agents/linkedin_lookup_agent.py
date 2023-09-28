from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from tools.tools import get_profile_url

from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name : str) -> str:
    """

    :param name:
    :return: Linkedin URL
    """
    llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    template="""
    given the full name {name_of_person} , I want you to get it me a link to their linked profile page. 
    Your answer should only contain URL"""

    tools_for_agent =[Tool(name='crawl google 4 linked profile page',
                           func=get_profile_url,
                           description = " useful for when you need to get the linkedin profile url of someone")]

    agent=initialize_agent(tools=tools_for_agent,llm=llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template=PromptTemplate(template=template, input_variables=['name_of_person'])


    linked_profile_url=agent.run(prompt_template.format(name_of_person=name))

    return linked_profile_url

