class Employee:
    employee_number = 0
    employee_name = ''
    age = 0
    sex = 0
    department = ''
    basic_salary = 0
    evaluation = 0

    def __init__(self, employee_number=0, employee_name='会社太郎'):
        self.employee_number = employee_number
        self.employee_name = employee_name

        print('従業員番号：' + str(employee_number) + '氏名：' + employee_name + 'の情報を管理します。\n')
        print('この社員に関するデータの入力は、set_employee_dataを実行してください。\n')
        print('set_employee_dataメソッドの詳細は以下の通りです。\n')
        print('age[int], sex[int:1(男性) or 2(女性)], department[st\nring], basic_salary[int], evaluation(int:1~3)\n')

    def set_employee_data(self, age, sex, department, basic_salary, evaluation):
        self.age = age
        self.sex = sex
        self.department = department
        self.basic_salary = basic_salary
        self.evaluation = evaluation
        
    def show_employee_data(self):
        print(str(self.employee_number))
        print(self.employee_name)
        print(str(self.age) + '歳')
        if(self.sex == 0):
            print('性別は未入力です')
        elif(self.sex == 1):
            print('男性')
        elif(self.sex == 2):
            print('女性')
        else:
            print('性別データが不正です')
        print(self.department)
        print('基本給：' + str(self.basic_salary) + '円')
        if(self.bonus == 0):
            print('ボーナスが未計算です。calc_bonusを実行し、ボーナス金額を確定させてください')
        else:
            print('ボーナス額：' + str(self.bonus) + '円')
        print('評価(1-3)' + str(self.evaluation))
        
    def calc_bonus(self):
        if(self.evaluation == 0):
            print('評価(1~3)が入力されていないので、bonusを算出できません。')
        elif((self.evaluation == 1) and (self.basic_salary != 0)):
            self.bonus = self.basic_salary * 1.5
        elif((self.evaluation == 2) and (self.basic_salary != 0)):
            self.bonus = self.basic_salary * 3
        elif((self.evaluation == 3) and (self.basic_salary != 0)):
            self.bonus = self.basic_salary * 5
        else:
            print('エラー：ボーナスの計算に失敗しました。')
    def save(self, filename):
        try:
            employee_file = open(filename, 'w')
            employee_file.write(
                '従業員番号：' + str(self.employee_number) + '\n' +
                '氏名：' + self.employee_name + '\n' +
                '年齢：' + str(self.age) + '/n'+
                '性別コード：' + str(self.sex) + '\n' +
                '所属：' + self.department + '\n' +
                '基本給:' + str(self.basic_salary) + '\n' +
                'ボーナス額：' + str(self.bonus) + '\n' +
                '評価：' + str(self.evaluation) + '\n'
            )
            employee_file.flush()
            employee_file.close()
            print('社員番号：' + str(self.employee_number) + '氏名：' + self.employee_name + 'の従業員データを保存しました。')
        except:
            print('save error')

emp = Employee(12345, '会社花子')
emp.set_employee_data(29, 2, '新規事業開発本部', 250000, 2)
emp.calc_bonus()
emp.show_employee_data()
emp.save('12345.txt')