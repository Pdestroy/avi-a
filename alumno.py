class estudiante():
  #atributos
  nombre="jose josua montoya bernal"
  promedio=9.7
  edad=17
  peso=45.7
  #metodos
  def inscripcion(self):
      print(f'{self.nombre} esta inscrito')
  def asesorias(self):
      print("el alumno no esta en asesorias")

alumno=estudiante()
alumno.inscripcion()
alumno.nombre="rosa ramos figueroa"
alumno.inscripcion()
