from setuptools import setup


setup(name = "clean_folder",
      version = "0.0.1",
      packages = ["clean_folder"],
      author = "Serhii Mamonov",
      description= "clean folder from trash",
      entry_points = {
          'console_scripts': ['clean-folder = clean_folder.clean:main'] 
      }         
)