# -*- coding: utf-8 -*-
"""
Estructura de datos bÃƒÂ¡sica de ÃƒÂ¡rbol binario.
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, element):
        if self.left is None:
            self.insert_left(element)
        
        elif self.right is None:
            self.insert_right(element)
        
        elif self.left.get_weight() <= self.right.get_weight() :
            self.left.insert(element)
        
        else:
            self.right.insert(element)
    
    def get_height(self):
        if self.left == None:
            altura_izq = 0
        else:
            altura_izq = self.left.get_height()
            
        if self.right == None:
            altura_drcha = 0
        else:
            altura_drcha=self.right.get_height()
        if altura_drcha< altura_izq:
            return 1 + altura_izq
        else:
            return 1 + altura_drcha
        
        
    def isbalanced(self):
        if self.left.get_height() is not None:
            altura_izq = self.left.get_height()

        else:
            altura_izq = 0
        if self.right.get_height() is not None:
            altura_drcha = self.right.get_height()
        else:
            altura_drcha = 0
        if abs(altura_izq - altura_drcha) <= 1:
            return True
        else:
            return False   
        izq_ok = True
        drcha_ok = True
        if self.left is not None:
    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            self.right.insert_right(data)

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            self.left.insert_left(data)

    def print_pre_order(self):
        # imprimir valor
        print(self.value)
        # imprimir rama izquierda
        if self.left is not None:
            self.left.print_pre_order()
        # imprimir rama derecha
        if self.right is not None:
            self.right.print_pre_order()

    def print_in_order(self):
        # imprimir rama izquierda
        if self.left is not None:
            self.left.print_in_order()
        # imprimir valor
        print(self.value)
        # imprimir rama derecha
        if self.right is not None:
            self.right.print_in_order()

    def print_post_order(self):
        # imprimir rama izquierda
        if self.left is not None:
            self.left.print_post_order()
        # imprimir rama derecha
        if self.right is not None:
            self.right.print_post_order()
        # imprimir valor
        print(self.value)

    def get_weight(self) -> int:
        weight = 1
        if self.left is not None:
            weight += self.left.get_weight()
        if self.right is not None:
            weight += self.right.get_weight()
        return weight

    def delete(self, data):
        data_node = None
        q = []
        q.append(self)
        temp = None
        while len(q):
            temp = q.pop(0)
            if temp.value == data:
                data_node = temp
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        if data_node:
            x = temp.value
            self.__delete_deepest(temp)
            data_node.value = x

    def __delete_deepest(self, to_delete):
        q = []
        q.append(self)
        while len(q):
            temp = q.pop(0)
            if temp is to_delete:
                temp = None
                return
            if temp.right is not None:
                if temp.right is to_delete:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left is not None:
                if temp.left is to_delete:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def __to_dict(self, preserve_empty=False) -> dict:
        """
        Crea una representaciÃƒÂ³n en diccionario del ÃƒÂ¡rbol, para usar con anytree.

        Parameters
        ----------
        preserve_empty : bool, optional
            Mostrar nodos vacÃƒÂ­os. El valor por defecto es False.

        Returns
        -------
        dict
            Una representaciÃƒÂ³n en diccionario del ÃƒÂ¡rbol.

        """
        data = {"name": self.value}
        if self.left is not None or self.right is not None or preserve_empty:
            data["children"] = []
        if self.left is not None:
            data["children"].append(self.left.__to_dict(preserve_empty))
        elif preserve_empty and self.right is not None:
            data["children"].append({"name": "VacÃƒÂ­o"})
        if self.right is not None:
            data["children"].append(self.right.__to_dict(preserve_empty))
        elif preserve_empty and self.left is not None:
            data["children"].append({"name": "VacÃƒÂ­o"})
        return data

    def pretty_print(self, preserve_empty=False):
        """
        Muestra una representaciÃƒÂ³n visual del ÃƒÂ¡rbol en la consola.

        Parameters
        ----------
        preserve_empty : bool, optional
            Mostrar nodos vacÃƒÂ­os. El valor por defecto es False.

        Returns
        -------
        None.

        """
        import importlib
        installed = importlib.util.find_spec("anytree")
        if installed is not None:
            from anytree import RenderTree
            from anytree.importer import DictImporter
            root = DictImporter().import_(self.__to_dict(preserve_empty))
            for pre, fill, node in RenderTree(root):
                print(f"{pre}{node.name}")
        else:
            print("LibrerÃƒÂ­a anytree no instalada")

    def export_dot(self, preserve_empty=False):
        """
        Imprime en la consola la representaciÃƒÂ³n dot del ÃƒÂ¡rbol.

        Parameters
        ----------
        preserve_empty : bool, optional
            Mostrar nodos vacÃƒÂ­os. El valor por defecto es False.

        Returns
        -------
        None.

        """
        import importlib
        installed = importlib.util.find_spec("anytree")
        if installed is not None:
            from anytree.exporter import DotExporter
            from anytree.importer import DictImporter
            root = DictImporter().import_(self.__to_dict(preserve_empty))
            for line in DotExporter(root, graph="graph", edgetypefunc=lambda n, c: "--"):
                print(line)
        else:
            print("LibrerÃƒÂ­a anytree no instalada")

    def to_image(self, filename="tree.png", preserve_empty=False):
        """
        Guarda el ÃƒÂ¡rbol en una imagen.

        graphviz tiene que estar instalado para que el mÃƒÂ©todo funcione.

        Parameters
        ----------
        filename : str, optional
            El nombre del archivo a crear. El valor por defecto es "tree.png".
        preserve_empty : bool, optional
            Mostrar nodos vacÃƒÂ­os. El valor por defecto es False.

        Returns
        -------
        None.

        """
        import importlib
        installed = importlib.util.find_spec("anytree")
        if installed is not None:
            from anytree.exporter import DotExporter
            from anytree.importer import DictImporter
            root = DictImporter().import_(self.__to_dict(preserve_empty))
            DotExporter(root).to_picture(filename)
        else:
            print("LibrerÃƒÂ­a anytree no instalada")

    def __get_edges(self) -> list:
        links = []
        if self.left is not None:
            links.append((self.value, self.left.value))
            links += self.left.__get_edges()
        if self.right is not None:
            links.append((self.value, self.right.value))
            links += self.right.__get_edges()
        return links

    def get_tree_string(self) -> str:
        """
        Devuelve una representaciÃƒÂ³n en cadena del ÃƒÂ¡rbol.

        ÃƒÅ¡sala en https://visualgo.net/en/graphds.
        La primera lÃƒÂ­nea contiene el peso del ÃƒÂ¡rbol y el nÃƒÂºmero de aristas,
        el resto de lÃƒÂ­neas son las aristas del ÃƒÂ¡rbol en orden izquierda-derecha.

        Returns
        -------
        str
            Cadena que representa el ÃƒÂ¡rbol.

        """
        edges = self.__get_edges()
        edges_str = f"{self.get_weight()} {len(edges)}\n"
        edges_str += "\n".join([f"{a} {b}" for a, b in self.__get_edges()])
        return edges_str


def create_tree_a():
    root = BinaryTree(1)
    root.insert_left(2)
    root.insert_right(3)
    root.right.insert_left(4)
    root.right.insert_right(5)
    return root


def create_tree_delete():
    root = BinaryTree(1)
    root.insert_left(2)
    root.left.insert_left(4)
    root.left.insert_right(5)
    root.insert_right(3)
    root.right.insert_left(6)
    root.right.insert_right(7)
    return root


def test():
    root = create_tree_a()
    print("pre:")
    root.print_pre_order()
    print()
    print("in:")
    root.print_in_order()
    print()
    print("post:")
    root.print_post_order()
    print()
    print("tree_str:")
    print(root.get_tree_string())

    print()
    print("prueba de eliminaciÃƒÂ³n")
    root = create_tree_delete()
    root.pretty_print()
    print(root.get_tree_string())
    root.delete(2)
    print("DespuÃƒÂ©s de eliminar:")
    print(root.get_tree_string())
    root.pretty_print()
    root.pretty_print(preserve_empty=True)


if __name__ == "__main__":
    test()