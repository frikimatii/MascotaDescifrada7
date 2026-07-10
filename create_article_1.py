import json
import os
from datetime import datetime

# Definimos el contenido HTML largo en una variable para evitar problemas de escape en JSON
contenido_html = """
<h2>Introducción</h2>
<p>Imagina esta escena: estás en el sofá, tu perro se acerca, le das unas suaves caricias en la cabeza y, de repente, lanza un bostezo enorme. Lo primero que piensas es que tiene sueño, pero acabáis de dar un largo paseo y ha dormido toda la tarde. Entonces, <strong>¿por qué mi perro bosteza cuando lo acaricio?</strong></p>
<p>El lenguaje corporal de los perros es fascinante y, a menudo, los humanos lo malinterpretamos. Mientras que para nosotros un bostezo es casi exclusivamente sinónimo de cansancio o aburrimiento, en el mundo canino es una herramienta de comunicación compleja y muy rica.</p>
<p>En este artículo de +COTAS, vamos a desgranar exactamente qué te está diciendo tu mejor amigo cuando bosteza bajo tus caricias, cómo aprender a leer sus señales y qué debes hacer (o dejar de hacer) para mejorar vuestro vínculo.</p>

<h2>¿Qué significa este comportamiento?</h2>
<p>Cuando un perro bosteza en respuesta a una interacción, como una caricia, un abrazo o incluso al hablarle de cerca, rara vez significa que tenga sueño. En el campo de la etología canina (el estudio del comportamiento de los perros), este tipo de bostezo se clasifica como una <strong>"señal de calma"</strong> o de apaciguamiento.</p>
<p>Las señales de calma son gestos que los perros utilizan para reducir la tensión social, mostrar que no son una amenaza, o intentar calmar a otros individuos (incluidos los humanos) o a sí mismos. Es su forma de decir: "Venga, relajémonos un poco".</p>
<p>Por lo tanto, si tu perro bosteza al acariciarlo, te está comunicando información vital sobre su estado emocional en ese preciso instante.</p>

<h2>¿Por qué sucede?</h2>
<p>Existen varias razones fundamentales por las que se desencadena este comportamiento durante las caricias:</p>
<ul>
    <li><strong>Sobrestimulación:</strong> A veces, las caricias son demasiado vigorosas, prolongadas o en zonas que al perro no le agradan especialmente (como la cabeza o las patas). El bostezo es una forma de liberar esa leve tensión.</li>
    <li><strong>Ansiedad leve o incomodidad:</strong> Si estás abrazando a tu perro (algo que a la mayoría no les gusta porque restringe su movimiento) o te inclinas directamente sobre él, puede sentirse invadido y bostezar para decirte: "Dame un poco de espacio, por favor".</li>
    <li><strong>Conflicto interno:</strong> Tu perro te quiere y quiere estar cerca de ti, pero quizás la forma en que lo estás tocando le resulta agobiante. El bostezo refleja ese choque entre querer la interacción y sentirse incómodo con ella.</li>
    <li><strong>Bostezo empático:</strong> ¡Sí, los perros también se contagian de nuestros bostezos! Si tú estabas relajado y bostezaste antes, él podría estar simplemente respondiendo empáticamente.</li>
</ul>

<h2>¿Es normal?</h2>
<p><strong>Completamente normal.</strong> De hecho, es una señal muy saludable. Un perro que bosteza para liberar estrés es un perro con buenas habilidades de comunicación. Está utilizando el lenguaje pacífico de su especie para gestionar una situación en lugar de recurrir a conductas más agresivas, como gruñir o morder.</p>

<h2>¿Cuándo debes preocuparte?</h2>
<p>Aunque el bostezo en sí es inofensivo, debes prestar atención si viene acompañado de otras señales de estrés o lenguaje corporal tenso. Si ignoras estas señales repetidamente, el perro podría escalar su comunicación. Preocúpate o detén la interacción si notas:</p>
<ul>
    <li>Se lame los labios constantemente (relamido de trufa).</li>
    <li>Voltea la cabeza o aparta la mirada de ti.</li>
    <li>Tiene el cuerpo rígido, las orejas pegadas hacia atrás o la cola entre las patas.</li>
    <li>Muestra la "mirada de ballena" (se ve el blanco de sus ojos porque gira el ojo sin girar la cabeza).</li>
    <li>Jadea de forma excesiva sin hacer calor ni haber hecho ejercicio.</li>
</ul>
<p><em>Nota importante: Si el bostezo es excesivo y constante, y va acompañado de letargo, dolor o falta de apetito, podría ser un signo de malestar físico. En ese caso, la recomendación de +COTAS es consultar siempre a tu veterinario de confianza.</em></p>

<h2>Errores comunes que cometemos</h2>
<p>Como humanos, somos primates, y nuestra forma natural de dar afecto es abrazar, apretar y tocar el rostro. Para los cánidos, esto puede ser antinatural. Los errores más comunes incluyen:</p>
<ul>
    <li><strong>Forzar el afecto:</strong> Obligar al perro a recibir besos o abrazos apretados.</li>
    <li><strong>Acariciar por encima de la cabeza:</strong> A muchos perros no les gusta que una mano venga desde arriba hacia su cabeza; lo perciben como una amenaza.</li>
    <li><strong>Ignorar el bostezo:</strong> Creer que tiene sueño y seguir abrazándolo, lo que aumenta su incomodidad.</li>
</ul>

<h2>Qué NO debes hacer</h2>
<p>Nunca debes regañar a tu perro por bostezar ni ignorar su incomodidad obligándole a soportar la caricia. Castigar las señales de calma es peligroso porque le enseñas al perro que "comunicarse pacíficamente no sirve de nada". Si le quitas el bostezo o el gruñido, la próxima vez podría saltar directamente a morder sin previo aviso.</p>

<h2>Qué sí puedes hacer (Consejos prácticos)</h2>
<p>Para mejorar la calidad de tus interacciones y asegurar que tu mascota realmente disfruta de tus mimos, aplica estos consejos prácticos:</p>
<ul>
    <li><strong>Haz la regla de los 3 segundos:</strong> Acaricia a tu perro durante tres segundos y para. Si él te busca, te empuja con el hocico o te da la pata, ¡quiere más! Si se aleja o bosteza, respeta su decisión y dale espacio.</li>
    <li><strong>Cambia la zona de las caricias:</strong> En lugar de la cabeza, prueba acariciar el pecho, los hombros o la base de la cola. Suelen preferir estas zonas.</li>
    <li><strong>Observa el panorama general:</strong> Evalúa su lenguaje corporal completo. Un perro relajado tendrá la boca ligeramente abierta, los músculos flojos y los ojos suaves.</li>
</ul>

<h2>Preguntas Frecuentes (FAQ)</h2>
<h3>¿Si mi perro bosteza mucho significa que está enfermo?</h3>
<p>No necesariamente, pero si los bostezos son incesantes, están fuera de contexto y vienen con letargo, temblores o problemas gastrointestinales, sí requiere atención veterinaria para descartar dolor u otras patologías.</p>
<h3>¿Los perros bostezan por aburrimiento?</h3>
<p>Sí, igual que nosotros. Si llevan horas sin hacer nada y bostezan acompañados de un gemido o estirándose, es muy probable que te estén pidiendo actividad o un paseo.</p>
<h3>¿Por qué mi perro bosteza cuando lo regaño?</h3>
<p>Es una señal de apaciguamiento clásica. Al bostezar, intenta calmar tu enfado y decirte "no soy una amenaza, por favor, relájate". No es un gesto de desobediencia o burla.</p>
<h3>¿Debo dejar de acariciar a mi perro si bosteza?</h3>
<p>Lo ideal es pausar unos segundos. Mira su reacción. Si se queda y te pide más, puedes continuar (quizás de forma más suave). Si se da la vuelta o se aleja, entonces sí, debías detenerte.</p>
<h3>¿Los bostezos de los perros son contagiosos?</h3>
<p>Estudios científicos indican que los perros pueden contagiarse de los bostezos humanos, especialmente de sus dueños, debido a la fuerte conexión empática que han desarrollado con nuestra especie a lo largo de miles de años de domesticación.</p>
<h3>¿Qué es el lenguaje de apaciguamiento canino?</h3>
<p>Son un conjunto de posturas y gestos (como bostezar, lamerse, girar la cabeza, caminar en curva, olfatear el suelo) que los perros usan para evitar conflictos y tranquilizar a otros individuos.</p>

<h2>Conclusión</h2>
<p>Entender <strong>por qué tu perro bosteza cuando lo acaricias</strong> es un paso gigante para convertirte en el mejor compañero posible para él. Al reconocer este sutil lenguaje de apaciguamiento, le demuestras que lo escuchas, que respetas sus límites y que su bienestar emocional es importante para ti. Así que la próxima vez que veas ese gran bostezo, sonríe, dale un poco de espacio si lo necesita, y maravíllate con la increíble capacidad de comunicación que tiene tu compañero de cuatro patas.</p>
"""

article = {
    "id": 11,
    "titulo": "¿Por qué mi perro bosteza cuando lo acaricio?",
    "slug": "por-que-mi-perro-bosteza-acaricio",
    "categoria": "Comportamiento",
    "fecha": "2023-12-05",
    "imagen": "img/perro-bosteza.webp",
    "descripcion": "Descubre qué significa realmente cuando tu perro bosteza al recibir caricias. Aprende a leer sus señales de calma y lenguaje corporal.",
    "seo": {
        "metaTitle": "¿Por qué mi perro bosteza cuando lo acaricio? | +COTAS",
        "metaDescription": "Si tu perro bosteza cuando lo acaricias, no siempre es sueño. Descubre el significado de las señales de calma y aprende a entender su lenguaje corporal.",
        "keywordPrincipal": "por que mi perro bosteza cuando lo acaricio",
        "keywords": [
            "señales de calma perros",
            "lenguaje corporal canino",
            "mi perro bosteza mucho",
            "perro bosteza acariciar",
            "estres en perros",
            "porque los perros bostezan",
            "etologia canina",
            "comportamiento de los perros",
            "perro incomodo caricias",
            "bostezo en perros"
        ]
    },
    "contenido": contenido_html,
    "amazon": [
        {
            "titulo": "Arnés antitirones acolchado (Para paseos sin estrés)",
            "url": "#"
        },
        {
            "titulo": "Libro de Lenguaje Corporal Canino (Recomendado)",
            "url": "#"
        }
    ]
}

# 1. Guardar el articulo en posts/
file_name = f"posts/{article['slug']}.json"
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(article, f, indent=2, ensure_ascii=False)

# 2. Actualizar data/posts-index.json
index_path = 'data/posts-index.json'
with open(index_path, 'r', encoding='utf-8') as f:
    index_data = json.load(f)

# Crear la entrada para el indice (sin contenido ni amazon)
index_entry = {
    "id": article["id"],
    "titulo": article["titulo"],
    "slug": article["slug"],
    "descripcion": article["descripcion"],
    "categoria": article["categoria"],
    "fecha": article["fecha"],
    "imagen": article["imagen"],
    "tags": ["perros", "comportamiento", "señales de calma"]
}

# Insertar al principio
index_data.insert(0, index_entry)

with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(index_data, f, indent=2, ensure_ascii=False)

print("Articulo creado exitosamente.")
