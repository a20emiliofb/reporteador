# Reporteador

## Funcionalidade e obxectivos

O obxectivo deste módulo é xestionar os erros que teñen os clientes. Así implementaremos as seguintes funcionalidades:
- Crear, editar e borrar reportes.
- Crear, editar e borrar clientes.
- Crear, editar e borrar empregados.

Así mesmo, compre extender o que significa un reporte e o que son os clientes e os empregados.    
Un reporte será un modelo que conteña información sobre un erro acontecido a un cliente. Así un reporte deberá gardar o título, unha descripción, a fecha na que ocorreu, a fecha na que soluciona o problema, quen o soluciona e, como non, o cliente o que lle ocorre.    
Os clientes e empregados son un modelo que extende a res.partner e que disporá de información booleana que nos informe se son clientes, empregados ou as dúas cousas a vez.

## Uso do módulo

1. Instalaremos o módulo buscando reporteador no buscador de módulos.

![Página instalación](https://user-images.githubusercontent.com/74708457/159156609-81f2f2e2-e4a2-4ec9-b16c-c5580dc660fa.png)

2. O pulsar no botón do menú lateral que pertence o módulo aparecerá a seguinte view.

![Página inicial](https://user-images.githubusercontent.com/74708457/159156497-f1977c18-00d0-45ea-bda9-d8387140c94f.png)

3.1. Se non temos empregados ou clientes crearémolos entrando nos submenús Empleados e Clientes.

![Menús](https://user-images.githubusercontent.com/74708457/159156808-bf25111e-ebb9-48cd-8881-6da0b0d5d6ad.png)

3.1.2. Engadiremos clientes ou empregados pulsando o botón crear e rellenamos os datos que queremos. Dependendo de se queremos un cliente, un empregado ou os dous pulsaremos os checkbox Cliente e Empleado

![Formulario empleado/cliente](https://user-images.githubusercontent.com/74708457/159156945-419afca9-1a65-4ef1-b62c-af7feaa5bc6e.png)

![Checkboxes para empleado/cliente](https://user-images.githubusercontent.com/74708457/159156967-19f028c8-c15a-4400-8e52-8e6493366714.png)

3.2. Se temos clientes e empregados podemos engadir os reportes que queiramos rellenando o seguinte formulario. Para entrar a este formulario é necesario volver o submenú Reportes e pulsar en Crear.

![Formulario reporte](https://user-images.githubusercontent.com/74708457/159157162-e45da177-58c8-4d1f-90b1-e5c3548dd5fb.png)

4. Unha vez creado aparecerá na lista dos reportes.

![Lista de reportes](https://user-images.githubusercontent.com/74708457/159157236-2607c45a-02ae-46e3-8675-93b4c546753e.png)

5. Para editar un reporte é necesario pulsar sobre o reporte que queiramos. Aparecerá unha vista cos detalles do reporte. Despois pulsar sobre Editar e cambiar os datos que queiramos. 

![Detalles do informe](https://user-images.githubusercontent.com/74708457/159157399-81c310c1-9483-4005-970b-a55a8cda8e0d.png)

![Edición do informe](https://user-images.githubusercontent.com/74708457/159157413-50051844-4eb5-4ad3-a54f-8163e9c1a369.png)
