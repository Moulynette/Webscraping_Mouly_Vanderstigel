import pandas as pd
from fastapi import FastAPI, Response

shein = pd.read_csv("files/shein.csv")
boohoo = pd.read_csv("files/bohoo_full2.csv")
df = (boohoo.append(shein)).reset_index().drop('index', axis = 1)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Everything is working!"}


@app.get("/all_clothes")
async def root():
    return {
        df.to_string()
    }

@app.get("/cheapest_t_shirt")
async def root():
    sub_df = (df.loc[df['Type'] == 'T-shirt']).reset_index()
    sub_df.sort_values(by=['Prix'],inplace=True)
    return {
        sub_df.head(1).to_string()
    }

@app.get("/cheapest_clothes")
async def root():
    sub_df = (df.sort_values(by=['Prix'])).reset_index()
    return {
        sub_df.head(5).to_string()
    }