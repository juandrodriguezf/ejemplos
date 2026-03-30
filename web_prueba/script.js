/*
 * INTERACTIVITY - STEP 3
 * Logic for dynamic elements
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("¡Script.js cargado correctamente!");
    console.log("Bienvenido al entorno de desarrollo web de Antigravity.");

    // Seleccionamos el botón principal
    const btnExplorar = document.getElementById('btn-explorar');

    // Añadimos una interacción al pulsar el botón
    if (btnExplorar) {
        btnExplorar.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Un pequeño efecto visual: cambiar el texto temporalmente
            const originalText = btnExplorar.innerText;
            btnExplorar.innerText = "¡Explorando...!";
            btnExplorar.style.filter = "hue-rotate(90deg)"; // Cambia el color del gradiente

            // Lanzamos una alerta de confirmación
            setTimeout(() => {
                alert("¡Bienvenido al futuro del desarrollo web con Antigravity! \n\nEl entorno está configurado y funcionando al 100%.");
                
                // Regresamos al estado original después de la alerta
                btnExplorar.innerText = originalText;
                btnExplorar.style.filter = "none";
            }, 500);
        });
    }

    // Un efecto sutil: cambio de estilo al hacer scroll
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('nav');
        if (window.scrollY > 50) {
            nav.style.backgroundColor = "rgba(15, 23, 42, 0.9)"; // Fondo más oscuro al bajar
            nav.style.backdropFilter = "blur(10px)";
            nav.style.borderBottom = "1px solid rgba(255, 255, 255, 0.1)";
        } else {
            nav.style.backgroundColor = "transparent";
            nav.style.borderBottom = "none";
        }
    });

});
