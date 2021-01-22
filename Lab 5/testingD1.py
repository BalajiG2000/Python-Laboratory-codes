D1={141152:"Sanjay Jain",141153:"Abhinav Agarwal",141154: "Abhishek Nigam",141155:" Aditya Arora",141156 :"Aditya Shrivastava",141157:" Aditya Thakur",
    141158:" Amit kumar",141159 :"Aashi Jain",
    141160 :"Deepak Singh",141161:" Mahendra Singh",141162:" Vijay Kumar "  ,141163 :"Aditya Pandey",141164 :"Aditya Kumar",141165:" Aditi Bhardwaj",
    141166:" Anup Kumar Nigam",141167 :"Abhishek Chatterjee",141168:" Abhimanyu Singh"}
D2={141152 :"Jhansi",141153:" Kanpur",141154:" Lucknow",141155 :"Agra",141156 :"Shimla",
        141157:" Chandigarh",141158 :"Mandi",141159 :"Kanpur",141160:" Mathura",141161:" Guna",
        141162:" Bhopal",141163:" Patna",141164 :"Gorakhpur",141165:" Lucknow",
        141166:" Kanpur",141167:" Nagpur",141168:" Bhopal"}
x=input("EnTER THE CITY YOU WANT TO FIND ENO NUM FOR :")
for key,value in D2.iteritems():
    if value==x:
        print key, D1.get(key)
