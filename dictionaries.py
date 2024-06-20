
student_info = {
"name": "john",
"age": "24",
"class": "12"
}

#print(student_info["name"])

ec2_instances_info = [
    {
        "id": "instance-001",
        "type": "t2.micro"
    },
    {
        "id": "instance-002",
        "type": "t2.medium"
    },
    {
        "id": "instance-003",
        "type": "t2.xlarge"
    }
]

print(ec2_instances_info[0]["type"])
print(ec2_instances_info[2]["id"])
