from sqlalchemy import create_engine,text

connection_string="mysql+pymysql://<username>:<password>@localhost:3306/<dbname>?charset=utf8mb4" # replace <username> ,<password> and <dbname> with your mysql datbase username,password and databasename respectively

engine=create_engine(connection_string,
                     connect_args={
                         "ssl":{
                             "ssl_ca":"/etc/ssl/cert.pem"
                         }
                     }
                     )

def fetch_jobs():
    with engine.connect() as conn:
        results=conn.execute(text("select * from jobs"))
        jobs=[]
        for i in results.all():
            jobs.append(i._asdict())
        return jobs

print(fetch_jobs())