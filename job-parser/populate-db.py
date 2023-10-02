from utils.parser import parseCompanyListing
import mysql.connector

def populateDB(link):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="jobTicker"
            )

    # creation of database
    # mycursor.execute("CREATE DATABASE jobTicker")
    mycursor = mydb.cursor()

    # create tables
    mycursor.execute("""CREATE TABLE companies
                     (company_name VARCHAR(255), company_link VARCHAR(255))
                     """)
    mycursor.execute("ALTER TABLE companies ADD UNIQUE INDEX(company_name)")
#
#    mycursor.execute("""CREATE TABLE company_locations
#                     (company_name VARCHAR(255), location VARCHAR(255))
#                     """)
#    mycursor.execute("""ALTER TABLE company_locations ADD UNIQUE
#                     INDEX(company_name, location)""")
#
    mycursor.execute("""CREATE TABLE company_positions
                     (position VARCHAR(255), company_name VARCHAR(255),
                      job_link VARCHAR(255))
                     """)
    mycursor.execute("""ALTER TABLE company_positions ADD UNIQUE
                     INDEX(company_name, position, job_link)""")

    companies = parseCompanyListing(link)

    for company in companies:
        mycursor.execute("""INSERT IGNORE INTO companies (company_name, company_link)
                         VALUES (%s, %s)""",
                         (company.name, company.link))
        for location in company.locations:
            mycursor.execute("""INSERT IGNORE INTO company_locations
                             (company_name, location) VALUES (%s, %s)""",
                             (company.name, location))
        for position in company.positions:
            mycursor.execute("""INSERT IGNORE INTO company_positions
                             (company_name, position, job_link) VALUES (%s, %s, %s)
                             """, (company.name, position[0], position[1]))
    mydb.commit()
    print("commited to database")

populateDB('https://github.com/ReaVNaiL/New-Grad-2024')
