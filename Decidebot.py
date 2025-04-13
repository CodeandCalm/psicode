# DecideBot: Simulador de decisiones morales (versión interactiva)
print("🤖 Hola! Soy DecideBot. Vamos a ver qué harías si te encontrás una billetera con plata 💸")
print("Contestá con 'sí' o 'no'... ¡sin miedo!\n")

# Función para capturar respuestas del usuario y convertirlas a True/False
def ask_belief(question):
    answer = input(question + " (sí/no): ").strip().lower()
    return answer == "sí"

# Recolectamos creencias
belief_honesty = ask_belief("¿Creés que ser honestx es importante?")
belief_nobody_saw_me = ask_belief("¿Pensás que nadie te vio?")
belief_need_the_money = ask_belief("¿Necesitás la plata?")
belief_consequences_exist = ask_belief("¿Te preocupa que haya consecuencias si te la quedás?")
belief_is_just_a_little = ask_belief("¿Pensás que es poca plata, no importa tanto?")
belief_karma_matters = ask_belief("¿Creés en el karma? (todo vuelve)")
belief_moral_responsibility = ask_belief("¿Sentís que hay que hacer lo correcto aunque nadie mire?")
belief_its_not_my_problem = ask_belief("¿Pensás que no es tu problema?")

print("\n🤔 Analizando tu perfil moral...\n")

# Decisión basada en combinaciones de creencias
if belief_honesty and belief_moral_responsibility and belief_karma_matters:
    print("✅ DECISIÓN: Devolvés la billetera. Alto nivel ético. Respeto 👏")
elif belief_nobody_saw_me and not belief_consequences_exist and belief_is_just_a_little:
    print("🤑 DECISIÓN: Te la quedás. La tentación ganó esta vez.")
elif belief_need_the_money and not belief_moral_responsibility:
    print("😕 DECISIÓN: Te la quedás, pero sabés que no está tan bien.")
elif belief_its_not_my_problem:
    print("🤷 DECISIÓN: Pasás de largo. Te desentendés del tema.")
else:
    print("😬 DECISIÓN: Duda moral. Te quedás pensándolo... eso también dice mucho.")

print("\n🤖 DecideBot: No hay respuestas perfectas, pero sí hay conciencia. ¡Gracias por jugarte!")
