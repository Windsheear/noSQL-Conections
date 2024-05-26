import redis

r = redis.Redis(
    host='redis-13250.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
    port=13250, 
    password='Waaf1QMVSKPoRpZVdYkxG3aZcsn9oBrM',
    db=0  # use the appropriate db number if 'cache-LWMOCOBQ' is not the first db
)

#create
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})
#read
r.hgetall('user-session:123')

#update

# set a key
# r.hset("person", "name", "jane")

#delete
r.delete("person") # delete a key
# r.hdel("person", "name") # delete a field



