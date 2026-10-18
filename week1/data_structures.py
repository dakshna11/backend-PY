users=["alice", "bob", "carol"]
users.append("dave")
users.remove("bob")
print(users[0], users[-1], users[1:3])

point=(10, 20)
x,y = point

user={"id": 1, "name": "Alice", "email": "alice@example.com"}
print(user["name"])
print(user.get("phone", "N/A")) #safe access
user["age"] = 25
for key, value in user.items():
    print(key, value)

tags={"python", "backend", "python"}
print(tags)
print({"a", "b"} & {"b", "c"}) #intersection

response={
    "status": "ok",
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
}
print(response["users"][1]["name"])

test=[{"name": "A", "score": 90}, {"name": "B", "score": 85}, {"name": "C", "score": 95}]
highest=test[0]["score"]
average=0
for item in test:
    average += item["score"]
    if(item["score"] > highest):  # noqa: PLR1730
        highest = item["score"]
print(highest)
print(average / len(test))