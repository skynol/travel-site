from pymongo import Connection

if __name__ == "__main__":
    con = Connection('0.0.0.0', 27017)

    db = con.test_database

    people = db.people

    #people.insert({'name':'Mike', 'food':'cheese'})
    #people.insert({'name':'John', 'food':'ham', 'Location':'UK'})
    #people.insert({'name':'Michelle', 'food':'cheese'})

    peeps = people.find()

    print "INSERT & FIND TEST"

    for person in peeps:
        if(person.name = "Mike")
        print person