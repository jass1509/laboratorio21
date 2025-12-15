class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"Libro '{self.titulo}' no disponible.")

    def devolver(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamanioMB):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamanioMB = tamanioMB

    def prestar(self):
        print(f"Libro digital '{self.titulo}' siempre disponible.")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_por_autor(self, autor):
        return [l for l in self.libros if l.autor == autor]

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.prestar()
                return
        print("Libro no encontrado")


# probando
biblio = Biblioteca()

biblio.agregar_libro(Libro("1984", "Orwell", 1949))
biblio.agregar_libro(Libro("El Quijote", "Cervantes", 1605))
biblio.agregar_libro(Libro("Fahrenheit 451", "Bradbury", 1953))
biblio.agregar_libro(LibroDigital("Python", "Guido", 2020, "PDF", 5))
biblio.agregar_libro(LibroDigital("Java", "James", 2019, "EPUB", 3))

biblio.listar_libros()
biblio.prestar_libro("1984")
biblio.prestar_libro("1984")

for _ in range(5):
    biblio.prestar_libro("Python")
print(biblio.buscar_por_autor("Orwell"))
 
libropedido=input("¿?que libro desea prestrase")
biblio.prestar_libro(libropedido)

