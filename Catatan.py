# command :
# install -> ip install "fastapi[standard]"
# execute script -> fastapi dev [nama_file].py

# mematikan server API diterminal dengan keyword (CTRL + C)

# import package
from fastapi import FastAPI, Header, HTTPException
import pandas as pd

# membuat object
app = FastAPI()

#membuat password
pasword= 12345

# endpoint -> standard untuk contoh : membuka halam utama (meminta data halaman utama)
# 1. http function
# 2. url yang bisa diakses oleh client
@app.get("/")
def getMain():
    # baca file csv -> pandas
    df = pd.read_csv('data.csv')

    # Misal ada filter, sort, dsb dilakukan sebelum function return

    return {
        "message" : "Hello World",
        "hasil": df.to_dict(orient="records")
    }

# setiap endpoint tidak boleh memiliki kombinasi http function url yang sama

# endpoint untuk mendapatkan data specific (filter)
# www.google.com/data/rajib -> response data rajib
# www.google.com/data/cleo -> response data cleo
# www.google.com/data/andre -> response eror (404 not found)
@app.get("/data/{username}")
def getData(username: str):
    # baca data file csv
    df = pd.read_csv('data.csv')

#melakukan filter 
    result = df.query(f"nama == '{username}'")


    return {"message": "Hello World", "hasil": result.to_dict(orient="records")}


# endpoint untuk melakukan function delete
# jika tidak ada api-key atau api-key != password maka responce eror
# jika ada dan sesuai maka lanjut delete -> success

@Catatan.delete("/data/{username}")
def deleteData(username: str, api_key: str = Header(None)):
    # cek authentication
    if api_key == None or api_key != password:
        # respon eror -> object HTTPException
        raise HTTPException(status_code=401, detail="authentication gagal") 


    #baca file csv -> pandas
    df = pd.read_csv('data.csv')
    # melakukan logic delete -> filter exclude
    result = df.query(f"nama != '{username}'")

    # write csv/ replace data baru
    #kasih index = false supaya index tidak masuk ke csv
    result.to_csv('data.csv', index=False)


    return {
        "message": "Hello World", 
        "hasil": result.to_dict(orient="records")
    }
