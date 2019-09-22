# Create your models here.


# deklaracija
from django.db import models
from django.utils import timezone


# tipi modelov


# klasa BP - main customer table [BP]
class BP(models.Model):
    # bp_id = models.IntegerField(max_length=6, primary_key= True)
    # models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bp_name = models.CharField(max_length=30)
    bp_vat = models.IntegerField(max_length=15)
    land = models.CharField(max_length=2)
    land_name = models.CharField(max_length=20)
    postal_code = models.IntegerField(max_length=10)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    person = models.CharField(max_length=20)
    person_title = models.CharField(max_length=20)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.EmailField()
    lang = models.CharField(max_length=2)
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.bp_name


# klasa FP - main Freigh-forwarder table[FP]
class FP(models.Model):
    # fp_id = models.IntegerField(primary_key=True)
    bp_id = models.ForeignKey(BP, on_delete=models.CASCADE)
    fp_name = models.CharField(max_length=30)
    fp_vat = models.IntegerField(max_length=15)
    land = models.CharField(max_length=2)
    land_name = models.CharField(max_length=20)
    postal_code = models.IntegerField(max_length=10)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    person = models.CharField(max_length=20)
    person_title = models.CharField(max_length=20)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.EmailField()
    lang = models.CharField(max_length=2)
    date = models.DateTimeField(default=timezone.now)
    ref_company1 = models.CharField(max_length=20)
    ref_company1_txt = models.TextField(max_length=200)
    ref_company2 = models.CharField(max_length=20)
    ref_company2_txt = models.TextField(max_length=200)
    ref_company3 = models.CharField(max_length=20)
    ref_company3_txt = models.TextField(max_length=200)


class groupage(models.Model):
    # bp_id = models.ForeignKey(BP, on_delete=models.CASCADE)
    fp_id = models.ForeignKey(FP, on_delete=models.CASCADE)
    # fp_id = models.IntegerField(primary_key=True)
    groupage_ldm = models.IntegerField()
    groupage_cbm = models.IntegerField()
    groupage_pallet_space = models.IntegerField()


class ltl(models.Model):
    # p_id = models.ForeignKey(BP, on_delete=models.CASCADE)
    fp_id = models.ForeignKey(FP, on_delete=models.CASCADE)
    # fp_id = models.IntegerField(primary_key=True)
    ltl_ldm = models.IntegerField()
    ltl_cbm = models.IntegerField()
    ltl_pallet_space = models.IntegerField()


class country_zone_postal(models.Model):
    # p_id = models.ForeignKey(BP, on_delete=models.CASCADE)
    fp_id = models.ForeignKey(FP, on_delete=models.CASCADE)
    #  fp_id = models.IntegerField(primary_key=True)
    country_select = [
        ('SI', 'Slovenia')
    ]
    country = models.CharField(max_length=2, choices=country_select)
    zone = models.IntegerField(max_length=2)
    postal_code = models.IntegerField(max_length=2)


# Excel import

class customer_current_price(models.Model):
    # p_id = models.ForeignKey(BP, on_delete=models.CASCADE)
    fp_id = models.ForeignKey(FP, on_delete=models.CASCADE)
    # fp_id = models.IntegerField(primary_key= True)
    transport_type_select = [
        ('01', 'Road-freight')
    ]
    transport_type = models.IntegerField(max_length=2, choices=transport_type_select)
    fp_text = models.CharField(max_length=15)
    country_from = models.CharField(max_length=2)
    postal_code_from = models.IntegerField(max_length=2)
    country_destination = models.CharField(max_length=2)
    postal_code_destination = models.IntegerField(max_length=2)
    weight = models.IntegerField()
    ldm = models.DecimalField(max_digits=3, decimal_places=1)
    cbm = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class base_price_list(models.Model):
    weight_choice = [
        ("20000", "20000kg"),
        ("17500", "17500kg"),
        ("15000", "15000kg"),
        ("12500", "12500kg"),
        ("10000", "10000kg"),
        ("7500", "7500kg"),
        ("5000", "5000kg"),
        ("3000", "3000kg"),
        ("2500", "2500kg"),
        ("2250", "2250kg"),
        ("2000", "2000kg"),
        ("1750", "1750kg"),
        ("1500", "1500kg"),
        ("1400", "1400kg"),
        ("1300", "1300kg"),
        ("1200", "1200kg"),
        ("1100", "1100kg"),
        ("1000", "1000kg"),
        ("900", "900kg"),
        ("800", "800kg"),
        ("700", "700kg"),
        ("600", "600kg"),
        ("500", "500kg"),
        ("450", "450kg"),
        ("400", "400kg"),
        ("350", "350kg"),
        ("300", "300kg"),
        ("250", "250kg"),
        ("200", "200kg"),
        ("175", "175kg"),
        ("150", "150kg"),
        ("125", "125kg"),
        ("100", "100kg"),
        ("75", "75kg"),
        ("50", "50kg"),
    ]

    weight = models.IntegerField(choices
                                 =weight_choice)
    country_zone_postal = models.DecimalField(max_digits=4,
                                              decimal_places=2)  # to mora dinamično polnit glede na podatke v count_zone_postal klasi

# https://pypi.org/project/django-countries/

# class Calculator(models.Model):
#
# class     a
