# Arquitectura-de-Software
Patrones de diseño
Service Locator: Es un patrón creacional que proporciona una manera centralizada de registrar y acceder a servicios sin acoplar directamente las clases que los usan.
Aplicación: Tenemos una clase central (ServiceLocator) que guarda servicios como pago y descuento. Así, podemos acceder desde cualquier parte del código sin acoplar directamente.

Adapter: Es un patrón estructural que permite adaptar la interfaz de una clase existente para que sea compatible con otra interfaz esperada.
Aplicación:  El CorreoExterno tiene su propio método. Creamos un adaptador para poder llamarlo como si fuera parte de nuestro sistema (enviar()).

Observer:Es un patrón de comportamiento que define una dependencia uno-a-muchos entre objetos, de manera que cuando uno cambia de estado, todos sus dependientes son notificados automáticamente.
Aplicación: cuando se crea una nueva función de teatro, todos los usuarios registrados reciben automáticamente la notificación sin tener que llamarlos uno por uno.
