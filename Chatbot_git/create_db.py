import pandas as pd
from sqlalchemy import create_engine
import os

class DatabaseFactory:
    def __init__(self,conn=None):
        if conn:
            self.engine = create_engine(conn)
        else:
            df = pd.read_csv("titanic.csv")
            print(df.shape)
            print(df.columns.tolist())
            #delete file titanic1.db if exists
            if os.path.exists("titanic1.db"):
                os.remove("titanic1.db")
            self.engine = create_engine("sqlite:///titanic1.db")
            df.to_sql("titanic", self.engine, index=False)
        self.chroma_db = None

    def get_engine(self):
        return self.engine
