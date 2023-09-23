from sqlalchemy import create_engine,text

connection_string="mysql+pymysql://root:admin#123@localhost:3306/careerwebsite?charset=utf8mb4" # replace <username> ,<password> and <dbname> with your mysql datbase username,password and databasename respectively

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


def fetch_job(id):
    with engine.connect() as conn:
        result=conn.execute(text("select * from jobs where id=:val").bindparams(val=id))
        rows=result.all()
        
        if len(rows)==0:
            return None
        
        else:
            return rows[0]._asdict()
        
        



