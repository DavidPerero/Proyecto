from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    dni = models.CharField(max_length=15, verbose_name='DNI o Cedula')
    email = models.EmailField(max_length=155, verbose_name='Correo Electronico')
    address = models.TextField(verbose_name="Direccion")
    phone = models.CharField(max_length=15, verbose_name="Telefono")
    avatar = models.ImageField(upload_to="avatar", verbose_name="Foto del Cliente", null=True, blank=True)
    created =models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated =models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "customer"
        ordering = ['-id']

class Cotizador(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Cliente")
    validity_date = models.DateField(verbose_name="Vigencia")
    term_days = models.PositiveIntegerField(verbose_name="Plazo (días)")
    expiration_date = models.DateField(verbose_name="Vencimiento")
    policy_type = models.CharField(max_length=100, verbose_name="Tipo de Póliza")
    insured_value = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor Asegurado")
    rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tasa (%)")
    minimum_premium = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prima Mínima", null=True, blank=True)
    premium = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prima", null=True, blank=True)
    extra_charge = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cargo Adicional", null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Derecho", null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="IVA (%)", null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return f"Cotizador {self.policy_type} - Cliente: {self.customer.name}"

    class Meta:
        verbose_name = "Cotizador de Seguro"
        verbose_name_plural = "Cotizador de Seguro"
        db_table = "Cotizador"
        ordering = ['-id']