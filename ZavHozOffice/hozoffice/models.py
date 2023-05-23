from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Workers(models.Model):
    employee_ID = models.IntegerField(default=0, primary_key=True) # Внутренний номер сотрудника
    # arr_responsible_asset_ID = models.ForeignKey(Assets, on_delete=models.CASCADE) # Список прикрепленного имущества   ХЗ жалуется что не видит Assets
    # arr_act_ID = models.ForeignKey(BaseActs, on_delete=models.CASCADE) # Список прикрепленных Актов                    ХЗ жалуется что не видит BaseActs
    personal_data_worker = models.CharField(max_length=200) # Личные данные сотрудника
    position_worker = models.CharField(max_length=100)  # Должность сотрудника
    higher_worker = models.CharField(max_length=100)  # Выше стоящий ответственный сотрудник
    work_department_worker = models.CharField(max_length=100) # Отдел сотрудника
    access_rights_worker = models.CharField(max_length=200) # Права доступа сотрудника
    employee_location_worker = models.CharField(max_length=100) # Местоположение сотрудника (кабинет, здание)

class Assets(models.Model):
    asset_ID = models.IntegerField(default=0, primary_key=True) # Внутренний инвентарный номер
    # дожлно быть так Responsible_Employee_ID = models.ForeignKey(Workers, on_delete=models.CASCADE) # на кого оформлен акт ! жалуется на
    Responsible_Employee_ID = models.IntegerField(default=0)
    # ActID = models.ForeignKey(BaseActs, on_delete=models.CASCADE)  # актуальный акт                                 ! жалуется что не видит BaseActs
    # asset_serial_ID = models.IntegerField(default=0)             # Серийный номер
    asset_name = models.CharField(max_length=100)			       # Название предмета(имущества)
    type_asset = models.CharField(max_length=100)                  # Тип имущества
    specifications_asset = models.CharField(max_length=200)  # Характеристики
    assigned_employee_asset	= models.IntegerField(default=0) # Закрепленный сотрудник (желательно с employee_ID)      !
    # responsible_asset = models.IntegerField(default=0) # Ответственный за Выдачу     (желательно с employee_ID)     !
    storage_location_asset = models.CharField(max_length=200) # Место хранения имуществ                               !
    storage_features_assets	= models.CharField(max_length=200) # Особенности хранения имущества
    # дожлно быть так current_act	= models.ForeignKey(Workers, on_delete=models.CASCADE) # Текущий акт приема - передачи #             ХЗ
    current_act = models.IntegerField(default=0) # Текущий акт приема - передачи
    # history_act = # История актов приема - передачи

class BaseActs(models.Model):
    act_ID = models.IntegerField(default=0, primary_key=True)  # Акт ID
    # предроложительная ошибка и от греха подальше responsible_employee_ID = models.ForeignKey(Workers, on_delete=models.CASCADE) # на кого оформлен акт
    responsible_employee_ID = models.IntegerField(default=0)   # на кого оформлен акт
    # предроложительная ошибка и от греха подальше asset_ID = models.ForeignKey(Assets, on_delete=models.CASCADE) # Предмет который участвуют в акте
    asset_ID = models.IntegerField(default=0)     # Предмет который участвуют в акте
    numbers_act = models.IntegerField(default=0)  # Кол-во актов
    last_act = models.IntegerField(default=0)     # Прошлый акт
    # ExampleAct = # Пример акта
    # responsible_current_act = models.ForeignKey(Workers, on_delete=models.CASCADE) # Ответственный за акт приема – передачи
    data_start_act = models.DateTimeField('date published') # Время и дата начала действия акта
