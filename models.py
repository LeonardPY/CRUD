


class Piple:

    def __init__(self,name,lastname,pasword) -> None:
        self.name = name
        self.lastname = lastname
        self.pasword = pasword


    def mongo_db(self):
        return {
            'имя':self.name,
            'фамилия':self.lastname,
            'Пароль':self.pasword
        }


        