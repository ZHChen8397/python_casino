from Member import Member
import csv
import os

FILE_PATH = os.path.join(os.getcwd(), "member_data.csv")


class Casino:
    def __init__(self):
        self.member_list = []
        self._load_member_data()

    def _load_member_data(self):
        with open("member_data.csv", newline="") as csvfile:
            member_data = csv.reader(csvfile)
            for member in member_data:
                tmp_member = eval(member[0])
                self.member_list.append(tmp_member)
        print(self.member_list)

    def _save_member_data(self):
        if os.path.isfile(FILE_PATH):
            with open("member_data.csv", "a+", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.member_list)
        else:
            with open("member_data.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.member_list)
    def get_member(self, name):
        for member in self.member_list:
            if member["Name"] == name:
                mem = Member(member["Name"], member["Gender"], member["Amount"], member["Record"], member["Level"])
                return mem
            else:
                return None

    def register_member(self):
        name, gender = input("請輸入姓名, 性別").split(",")
        member = Member(name, gender)
        member_data = {"Name": member.name, "Gender": member.gender, "Amount": member.amount, \
                    "Record": member.record, "Level": member.level}
        self.member_list.append(member_data)
        self._save_member_data()
        return member


def main():
    option = 0
    member = None
    casino = Casino()   
    while option != -1:
        print("Welcome!")
        name = input("Please input your name! \n")
        member = casino.get_member(name)
        if member == None:
            is_register_member = input("you're not a member, do you want to register? Yes | No \n")
            member = casino.register_member() if is_register_member == "Yes" else quit()
        print("Hello Mr.{}".format(member.name)) if member.gender == "man" else print("Hello Miss.{}".format(member.name))
        print("How can I help you?")
        option = input("1. Record \n 2. Deposit Amount \n3. Play games!\n -1. Leave!!:\n")
        

if __name__ == "__main__":
    main()