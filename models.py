from collections import namedtuple


Person=namedtuple("Person",['email','first_name','last_name','age'])

data={
    1:Person("johndoe@gmail.com","John","Doe",23),
    2:Person("jerryblue@gmail.com","Jerry","blue",24),
    3:Person("jasonross@gmail.com","Jasson","ross",25),
    4:Person("brucewayne@gmail.com","Bruce","Wayne",30),
}