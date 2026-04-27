# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):

    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):

    return price * (1 + tax_pct / 100)



def final_price(price, quantity, discount_pct, tax_pct):
    """
    Calcula el precio final de una compra.
    Debe USAR las funciones apply_discount y apply_tax.

    Pasos:
      1. Calcular el subtotal (price * quantity).
      2. Aplicar el descuento al subtotal usando apply_discount.
      3. Aplicar el impuesto al resultado usando apply_tax.
      4. Retornar el resultado redondeado a 2 decimales usando round().
    """
    subtotal = price * quantity

    con_descuento = apply_discount(subtotal, discount_pct)

    con_impuesto = apply_tax(con_descuento, tax_pct)

    return round(con_impuesto, 2)

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    """
    Dados dos productos A y B (cada uno con su precio, cantidad y descuento)
    y un porcentaje de impuesto común, retorna el string "A" o "B"
    según cuál tenga el menor precio final.
    Si son iguales, retorna "A".
    Debe USAR la función final_price para resolver el ejercicio.
    """
    final_pricea = final_price(price_a, qty_a, disc_a, tax_pct)
    final_priceb = final_price(price_b, qty_b, disc_b, tax_pct)

    if final_pricea <= final_priceb:
        return "A"
    else:
        return "B"


    return "ANSWER HERE"  # Remove this line and implement
