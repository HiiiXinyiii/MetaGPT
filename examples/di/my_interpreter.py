import asyncio

from metagpt.schema import Message
from metagpt.logs import logger
from metagpt.roles.di.data_interpreter import DataInterpreter
from metagpt.utils.recovery_util import save_history

import pandas as pd

async def main(requirement: str = ""):
    di = DataInterpreter()
    
    # data = pd.read_csv('E:/Capstone/data/recentT6.csv')
    # data_message = Message(content=f"{data}", role="user")
    # di.put_message(data_message)

    rsp = await di.run(requirement)
    logger.info(rsp)
    save_history(role=di)

def ask(requirement: str = ""):
    def template(reuqirement: str):
        new_reuqirement = f"{reuqirement}."\
            f"If given a file path, please read the data file from that path and answer the question. If given a database table, lease read from the database table by SQL."\
            f"You also do not have to use only the information here to answer questions - you can run intermediate queries to do exporatory data analysis to give you more information as needed."
        return new_reuqirement
        
    requirement = template(requirement)

    asyncio.run(main(requirement))



if __name__ == "__main__":
    requirement = f"How many records in this data E:/Capstone/data/recentT6.csv?"
    # requirement = f"Show me the pie chart about the different value percentage of ON_HOLD field in this dataset E:/Capstone/data/recentT6.csv."
    requirement = f"How many records in this data D:/Capstone/data/recentT6.csv? And then show me the pie chart about the different value percentage of ON_HOLD field in this dataset."
    Q1 = "What is the 2024 forecast for TFNA in this data file D:/Capstone/data"
    ask(requirement)

