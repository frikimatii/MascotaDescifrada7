import json
import os

posts = [
    {
        "id": "1",
        "titulo": "¿Por qué los gatos amasan?",
        "slug": "por-que-los-gatos-amasan",
        "descripcion": "Descubre las razones instintivas y emocionales por las que tu gato te amasa como si fuera pan.",
        "categoria": "Gatos",
        "fecha": "2023-10-15",
        "imagen": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "3 min",
        "destacado": True,
        "tags": ["gatos", "comportamiento", "felinos"],
        "contenido": "<h2>El instinto desde cachorros</h2><p>Cuando son apenas unos recién nacidos, los gatitos amasan el vientre de su madre para estimular la producción de leche. Este comportamiento está profundamente arraigado en su instinto de supervivencia.</p><h2>Es una muestra de afecto</h2><p>Si tu gato te amasa, siéntete afortunado. Es una forma de decir que se siente seguro y cómodo contigo, tal como se sentía con su madre.</p><h2>Marcaje de territorio</h2><p>Los gatos tienen glándulas odoríferas en las almohadillas de sus patas. Al amasar, liberan feromonas que marcan la superficie (o a ti) como su propiedad.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Cama relajante para gatos",
                "descripcionCorta": "Cama antiestrés suave y cómoda, ideal para que tu gato amase y descanse plácidamente.",
                "url": "#"
            }
        ]
    },
    {
        "id": "2",
        "titulo": "¿Por qué tu perro te mira fijamente?",
        "slug": "por-que-tu-perro-te-mira-fijamente",
        "descripcion": "Esa mirada profunda de tu perro significa mucho más de lo que crees. Aquí te explicamos los motivos.",
        "categoria": "Perros",
        "fecha": "2023-10-18",
        "imagen": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "4 min",
        "destacado": True,
        "tags": ["perros", "comportamiento", "caninos"],
        "contenido": "<h2>Busca tu atención o comida</h2><p>La razón más común es simple: quiere algo. Ya sea un paseo, caricias o ese pedazo de comida que tienes en la mano.</p><h2>Amor y conexión (La hormona del amor)</h2><p>Estudios científicos han demostrado que cuando los perros y los humanos se miran a los ojos, ambos liberan oxitocina, conocida como la hormona del amor o del vínculo.</p><h2>Trata de entenderte</h2><p>Los perros son expertos leyendo el lenguaje corporal humano. A menudo te miran fijamente para descifrar tu estado de ánimo o anticipar tu próximo movimiento.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/61M63eLqN0L._AC_SL1500_.jpg",
                "nombre": "Premios saludables para perros",
                "descripcionCorta": "Snacks naturales perfectos para recompensar a tu perro cuando te preste atención.",
                "url": "#"
            }
        ]
    },
    {
        "id": "3",
        "titulo": "La mejor dieta para loros",
        "slug": "mejor-dieta-loros",
        "descripcion": "Alimentar a un loro correctamente es fundamental para su plumaje y longevidad.",
        "categoria": "Aves",
        "fecha": "2023-11-01",
        "imagen": "https://images.unsplash.com/photo-1552728089-571681137f68?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Dr. Plumas",
        "tiempoLectura": "5 min",
        "destacado": False,
        "tags": ["aves", "alimentacion", "loros"],
        "contenido": "<h2>Más allá de las semillas</h2><p>Un error común es alimentar a los loros solo con semillas de girasol. Esto provoca deficiencias nutricionales graves y obesidad.</p><h2>Frutas y verduras frescas</h2><p>Deberían componer al menos el 40% de su dieta. Manzana, zanahoria, brócoli y pimientos son excelentes opciones.</p><h2>Pellets formulados</h2><p>Los piensos o pellets de alta calidad aseguran que tu loro reciba todas las vitaminas y minerales necesarios en cada bocado.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Pienso NutriBird para loros",
                "descripcionCorta": "Alimento completo y balanceado para loros medianos y grandes.",
                "url": "#"
            }
        ]
    },
    {
        "id": "4",
        "titulo": "Cómo preparar el acuario para un pez Betta",
        "slug": "preparar-acuario-pez-betta",
        "descripcion": "Los Bettas no deben vivir en vasos de agua. Te enseñamos a crear su hogar ideal.",
        "categoria": "Peces",
        "fecha": "2023-11-05",
        "imagen": "https://images.unsplash.com/photo-1524704654690-b56c05c78a00?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "6 min",
        "destacado": True,
        "tags": ["peces", "acuario", "betta"],
        "contenido": "<h2>El tamaño importa</h2><p>Un pez Betta necesita un acuario de al menos 15 o 20 litros. Olvídate de las pequeñas peceras redondas sin filtro.</p><h2>Filtración y temperatura</h2><p>El agua debe estar entre 24°C y 27°C. Un filtro suave es esencial, ya que los Bettas prefieren aguas tranquilas sin mucha corriente.</p><h2>Decoración segura</h2><p>Evita plantas de plástico duro que puedan rasgar sus delicadas aletas. Opta por plantas naturales o de seda, y provee escondites.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Kit Acuario 20L",
                "descripcionCorta": "Acuario de cristal con filtro de cascada suave e iluminación LED.",
                "url": "#"
            }
        ]
    },
    {
        "id": "5",
        "titulo": "Cuidados básicos de una tortuga de agua",
        "slug": "cuidados-basicos-tortuga-agua",
        "descripcion": "Las tortugas son mascotas fascinantes pero requieren cuidados específicos de luz y agua.",
        "categoria": "Reptiles",
        "fecha": "2023-11-10",
        "imagen": "https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "4 min",
        "destacado": False,
        "tags": ["reptiles", "tortugas", "agua"],
        "contenido": "<h2>El hábitat adecuado</h2><p>Necesitan un acua-terrario espacioso. Una regla general es 40 litros de agua por cada 2.5 cm de caparazón.</p><h2>Zona seca y asoleamiento</h2><p>Es indispensable proporcionar una rampa hacia una zona completamente seca. Aquí es donde se secarán para evitar hongos y absorberán la luz.</p><h2>Iluminación UVB</h2><p>La luz UVB es crítica para que puedan metabolizar el calcio y mantener un caparazón duro y sano. Sin ella, desarrollarán enfermedades óseas.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Lámpara UVB para reptiles",
                "descripcionCorta": "Foco de espectro completo esencial para la salud del caparazón.",
                "url": "#"
            }
        ]
    },
    {
        "id": "6",
        "titulo": "¿Cuándo llevar a tu conejo al veterinario?",
        "slug": "cuando-llevar-conejo-veterinario",
        "descripcion": "Los conejos ocultan sus enfermedades. Aprende a detectar los signos de alarma.",
        "categoria": "Salud",
        "fecha": "2023-11-12",
        "imagen": "https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "4 min",
        "destacado": False,
        "tags": ["conejos", "salud", "veterinario"],
        "contenido": "<h2>Parada intestinal</h2><p>Si tu conejo deja de comer o hacer caca por más de 12 horas, es una emergencia médica. El estasis gastrointestinal es fatal si no se trata rápido.</p><h2>Problemas dentales</h2><p>Los dientes de los conejos nunca dejan de crecer. Si notas babeo, pérdida de apetito o lagrimeo excesivo, sus muelas podrían estar sobrecrecidas.</p><h2>Cambios de comportamiento</h2><p>Un conejo letárgico, que rechina los dientes de forma fuerte (señal de dolor) o que se aísla, necesita revisión inmediata por un veterinario de exóticos.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Heno Timothy de primera calidad",
                "descripcionCorta": "Indispensable para mantener el desgaste dental y la digestión sana.",
                "url": "#"
            }
        ]
    },
    {
        "id": "7",
        "titulo": "Beneficios de pasear a tu perro todos los días",
        "slug": "beneficios-pasear-perro",
        "descripcion": "El paseo es mucho más que ir al baño. Es vital para la salud mental de tu perro.",
        "categoria": "Perros",
        "fecha": "2023-11-15",
        "imagen": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "3 min",
        "destacado": False,
        "tags": ["perros", "salud", "ejercicio"],
        "contenido": "<h2>Estimulación mental</h2><p>Olfatear es el equivalente a leer el periódico para los perros. Necesitan procesar los olores de su entorno para mantener su cerebro activo.</p><h2>Control de peso y salud cardiovascular</h2><p>El ejercicio regular previene la obesidad, problemas articulares y mejora la función del corazón de tu mascota (y la tuya).</p><h2>Socialización</h2><p>Ver a otros perros, personas y escuchar ruidos de la calle ayuda a prevenir fobias y problemas de agresión por miedo.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Arnés antitirones acolchado",
                "descripcionCorta": "Paseos cómodos y sin ahogos para ti y tu mejor amigo.",
                "url": "#"
            }
        ]
    },
    {
        "id": "8",
        "titulo": "Plantas tóxicas para los gatos",
        "slug": "plantas-toxicas-gatos",
        "descripcion": "Protege a tu minino conociendo qué plantas comunes pueden ser letales.",
        "categoria": "Gatos",
        "fecha": "2023-11-20",
        "imagen": "https://images.unsplash.com/photo-1513245543132-31f507417b26?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "5 min",
        "destacado": True,
        "tags": ["gatos", "salud", "prevencion"],
        "contenido": "<h2>Lirios (Lilium)</h2><p>Son extremadamente tóxicos. Incluso morder una hoja o lamer el polen de su pelaje puede causar fallo renal agudo en menos de 3 días.</p><h2>Monstera deliciosa (Costilla de Adán)</h2><p>Contiene cristales de oxalato de calcio. Morderla causa irritación intensa en la boca, salivación excesiva y vómitos.</p><h2>Aloe Vera</h2><p>Aunque es curativa para humanos, la savia amarilla debajo de la piel del Aloe es tóxica para perros y gatos, causando letargo y diarrea.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Hierba gatera cultivable",
                "descripcionCorta": "Semillas de Catnip orgánico para que tu gato purgue de forma segura.",
                "url": "#"
            }
        ]
    },
    {
        "id": "9",
        "titulo": "Errores comunes al alimentar peces",
        "slug": "errores-alimentar-peces",
        "descripcion": "Dar demasiada comida es la causa número uno de muerte en acuarios caseros.",
        "categoria": "Alimentación",
        "fecha": "2023-11-22",
        "imagen": "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "3 min",
        "destacado": False,
        "tags": ["peces", "alimentacion", "cuidados"],
        "contenido": "<h2>La sobrealimentación</h2><p>Los peces parecen tener siempre hambre, pero sus estómagos son del tamaño de uno de sus ojos. La comida que sobra se pudre y genera amoníaco tóxico.</p><h2>Falta de variedad</h2><p>Dar siempre las mismas hojuelas comerciales aburre a los peces y puede causarles deficiencias. Intercala con alimento vivo o congelado.</p><h2>La regla de los 2 minutos</h2><p>Si tus peces no se han comido toda la comida en 2 minutos, les has dado demasiada. Retira el sobrante con una red.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Comida premium en gránulos",
                "descripcionCorta": "Gránulos de hundimiento lento que ensucian menos el agua.",
                "url": "#"
            }
        ]
    },
    {
        "id": "10",
        "titulo": "Señales de estrés en tu mascota",
        "slug": "senales-estres-mascota",
        "descripcion": "Identifica rápidamente si tu perro o gato está sufriendo de ansiedad.",
        "categoria": "Comportamiento",
        "fecha": "2023-11-25",
        "imagen": "https://images.unsplash.com/photo-1450778869180-41d0601e046e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "autor": "Admin",
        "tiempoLectura": "5 min",
        "destacado": True,
        "tags": ["estres", "comportamiento", "psicologia"],
        "contenido": "<h2>En perros</h2><p>Bostezos fuera de contexto, relamerse el hocico constantemente, jadeos sin haber hecho ejercicio, o destructividad repentina en casa.</p><h2>En gatos</h2><p>Acicalamiento excesivo (llegando a arrancarse pelo), orinar fuera de la caja de arena, esconderse por mucho tiempo o maullar compulsivamente.</p><h2>Qué hacer</h2><p>Evita regañarlos, ya que aumentará la ansiedad. Busca la causa (mudanza, ruidos, falta de rutina) y considera usar difusores de feromonas o consultar a un etólogo.</p>",
        "productosAmazon": [
            {
                "imagen": "https://m.media-amazon.com/images/I/71Xm3x454JL._AC_SL1500_.jpg",
                "nombre": "Difusor Feliway / Adaptil",
                "descripcionCorta": "Feromonas sintéticas que proporcionan un mensaje de seguridad.",
                "url": "#"
            }
        ]
    }
]

# Guardar los 10 posts en la carpeta posts
for post in posts:
    with open(f"posts/{post['slug']}.json", "w", encoding="utf-8") as f:
        json.dump(post, f, indent=2, ensure_ascii=False)

# Crear el index
index_data = []
for post in posts:
    index_entry = {k: v for k, v in post.items() if k not in ["contenido", "productosAmazon"]}
    index_data.append(index_entry)

with open("data/posts-index.json", "w", encoding="utf-8") as f:
    json.dump(index_data, f, indent=2, ensure_ascii=False)

print("Posts generados exitosamente.")
