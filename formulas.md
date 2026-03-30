# Ejemplos de Ecuaciones en Antigravity (LaTeX)

Este archivo muestra cómo usar la sintaxis de **LaTeX** para renderizar ecuaciones matemáticas dentro de archivos Markdown (`.md`).

---

## 1. Ecuaciones en Línea (Inline Math)
Para insertar ecuaciones dentro de un texto, se usan los símbolos `$` al principio y al final.

- **Fórmula de la Relatividad**: La energía se define como $E = mc^2$.
- **Teorema de Pitágoras**: En un triángulo rectángulo, $a^2 + b^2 = c^2$.
- **Función Exponencial**: El límite es $\lim_{n \to \infty} (1 + \frac{1}{n})^n = e$.

---

## 2. Bloques de Ecuaciones (Block Math)
Para que las ecuaciones aparezcan centradas y en su propia línea, se usan dobles símbolos `$$`.

### Integral de Gauss
$$ \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi} $$

### Fórmula Cuadrática
$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

### Identidad de Euler
$$ e^{i\pi} + 1 = 0 $$

---

## 3. Elementos Comunes y Útiles

### Sumatorias y Productorias
- **Sumatoria**: $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$
- **Productoria**: $\prod_{i=1}^{k} a_i$

### Matrices
$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

### Alineación de Ecuaciones (Multilínea)
$$
\begin{aligned}
(a+b)^2 &= (a+b)(a+b) \\
&= a^2 + ab + ba + b^2 \\
&= a^2 + 2ab + b^2
\end{aligned}
$$

---

## ✍️ Nota para el Usuario
Puedes editar este archivo y cualquier cambio que hagas en el formato LaTeX se renderizará automáticamente en la vista previa del editor de Antigravity.
