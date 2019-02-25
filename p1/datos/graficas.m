uEmisor = load("EmisorUniformeCast.txt");
uReceptor = load("ReceptorUniformeCast.txt");
gEmisor = load("EmisorGaussCast.txt");
gReceptor = load("ReceptorGaussCast.txt");

figure(1)
hist(uEmisor)
title("Emisor con distribucion uniforme")
xlabel("Tiempo (s)")
xlabel("Nº paquetes")

figure(2)
hist(uReceptor)
title("Emisor con distribucion uniforme")
xlabel("Tiempo (s)")
xlabel("Nº paquetes")

figure(3)
hist(gEmisor)
title("Emisor con distribucion gaussiana")
xlabel("Tiempo (s)")
xlabel("Nº paquetes")

figure(4)
hist(gReceptor)
title("Emisor con distribucion gaussiana")
xlabel("Tiempo (s)")
xlabel("Nº paquetes")
