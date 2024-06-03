
from dataclasses import dataclass


@dataclass
class Vacante:
    id:str
    titulo:str
    ciudad:str
    url: str
    categoria:str
    subcategoria:str
    educacion:str
    detalles:list
    descripcion:str

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ciudad": self.ciudad,
            "url": self.url,
            "categoria": self.categoria,
            "educacion": self.educacion,
            "subcategoria": self.subcategoria,
            "detalles": self.detalles,
            "descripcion": self.descripcion.replace("\\n", " ")
        }