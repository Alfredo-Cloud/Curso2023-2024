{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nOOPLCHF7hLB"
      },
      "source": [
        "**Task 06: Modifying RDF(s)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "Yl9npCt8n6m-"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: rdflib in c:\\users\\usuario\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (7.0.0)\n",
            "Requirement already satisfied: isodate<0.7.0,>=0.6.0 in c:\\users\\usuario\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from rdflib) (0.6.1)\n",
            "Requirement already satisfied: pyparsing<4,>=2.1.0 in c:\\users\\usuario\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from rdflib) (3.0.9)\n",
            "Requirement already satisfied: six in c:\\users\\usuario\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\\localcache\\local-packages\\python311\\site-packages (from isodate<0.7.0,>=0.6.0->rdflib) (1.16.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install rdflib\n",
        "github_storage = \"https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XY7aPc86Bqoo"
      },
      "source": [
        "Read the RDF file as shown in class"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "9ERh415on7kF"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<Graph identifier=N3e6177398a444513964790d6e832dc27 (<class 'rdflib.graph.Graph'>)>"
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "from rdflib import Graph, Namespace, Literal\n",
        "from rdflib.namespace import RDF, RDFS\n",
        "g = Graph()\n",
        "g.namespace_manager.bind('ns', Namespace(\"http://somewhere#\"), override=False)\n",
        "g.namespace_manager.bind('vcard', Namespace(\"http://www.w3.org/2001/vcard-rdf/3.0#\"), override=False)\n",
        "g.parse(github_storage+\"/rdf/example5.rdf\", format=\"xml\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gM3DASkTQQ5Y"
      },
      "source": [
        "Create a new class named Researcher"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "6vtudax8Xb7b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "ns = Namespace(\"http://somewhere#\")\n",
        "g.add((ns.Researcher, RDF.type, RDFS.Class))\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qp1oe2Eddsvo"
      },
      "source": [
        "**TASK 6.1: Create a new class named \"University\"**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "pnsrsgRUWF3A"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://somewhere#University http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "g.add((ns.University, RDF.type, RDFS.Class))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MXBqtBkJd22I"
      },
      "source": [
        "**TASK 6.2: Add \"Researcher\" as a subclass of \"Person\"**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "53hZNtXsXCNq"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#Researcher http://www.w3.org/2000/01/rdf-schema#subClassOf http://xmlns.com/foaf/0.1/Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://somewhere#University http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "from rdflib.namespace import FOAF   #Soy mas partidario de poner todos los imports al principio pero lo pongo aqui por no tocar la base del ejercicio\n",
        "g.add((ns.Researcher, RDFS.subClassOf, FOAF.Person))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OGct6k7Ld9O0"
      },
      "source": [
        "**TASK 6.3: Create a new individual of Researcher named \"Jane Smith\"**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "jbMMSHSZcFcf"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#JaneSmith http://xmlns.com/foaf/0.1/name Jane Smith\n",
            "http://somewhere#Researcher http://www.w3.org/2000/01/rdf-schema#subClassOf http://xmlns.com/foaf/0.1/Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://somewhere#JaneSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Resercher\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://somewhere#University http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "from rdflib.namespace import XSD\n",
        "g.add((ns.JaneSmith, RDF.type ,ns.Resercher))\n",
        "g.add((ns.JaneSmith, FOAF.name, Literal(\"Jane Smith\", datatype=XSD.string)))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tD383J__eHfV"
      },
      "source": [
        "**TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "hWmwlAfBcgN-"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#JaneSmith http://xmlns.com/foaf/0.1/name Jane Smith\n",
            "http://somewhere#Researcher http://www.w3.org/2000/01/rdf-schema#subClassOf http://xmlns.com/foaf/0.1/Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#Given Jane\n",
            "http://somewhere#JaneSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Resercher\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#FN Jane Smith\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#EMAIL jsmith@gmail.com\n",
            "http://somewhere#University http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#familyname Smith\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "VCARD = Namespace(\"http://www.w3.org/2001/vcard-rdf/3.0#\")  #Creamos un name con la uri base de lo que queremso describir\n",
        "g.add((ns.JaneSmith, VCARD.EMAIL, Literal(\"jsmith@gmail.com\", datatype = XSD.string)))\n",
        "g.add((ns.JaneSmith, VCARD.FN, Literal(\"Jane Smith\", datatype = XSD.string)))\n",
        "g.add((ns.JaneSmith, VCARD.Given, Literal(\"Jane\", datatype = XSD.string)))\n",
        "g.add((ns.JaneSmith, VCARD.familyname, Literal(\"Smith\", datatype = XSD.string)))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GyZOMndoeUj4"
      },
      "source": [
        "**TASK 6.5: Add UPM as the university where John Smith works**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "VZUhnfLWd3x-"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#JaneSmith http://xmlns.com/foaf/0.1/name Jane Smith\n",
            "http://somewhere#Researcher http://www.w3.org/2000/01/rdf-schema#subClassOf http://xmlns.com/foaf/0.1/Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#Given Jane\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0#worksAt http://somewhere#UPM\n",
            "http://somewhere#JaneSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Resercher\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#UPM http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#University\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#FN Jane Smith\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#EMAIL jsmith@gmail.com\n",
            "http://somewhere#University http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#familyname Smith\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "g.add((ns.UPM, RDF.type, ns.University))\n",
        "g.add((ns.JohnSmith, VCARD.worksAt, ns.UPM))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Kl66UsPtSIhG"
      },
      "source": [
        "**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "Eapw6FTPSTJK"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "http://somewhere#JaneSmith http://xmlns.com/foaf/0.1/name Jane Smith\n",
            "http://somewhere#Researcher http://www.w3.org/2000/01/rdf-schema#subClassOf http://xmlns.com/foaf/0.1/Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Given John\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#Given Jane\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0#worksAt http://somewhere#UPM\n",
            "http://somewhere#JaneSmith http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Resercher\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#UPM http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#University\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Family Jones\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#FN Jane Smith\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/Family Smith\n",
            "http://somewhere#Jown http://xmlns.com/foaf/0.1/knows http://somewhere#JaneSmith\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Property\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/Given Sara\n",
            "http://somewhere#SaraJones http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://somewhere#Person\n",
            "http://somewhere#JohnSmith http://www.w3.org/2001/vcard-rdf/3.0/FN John Smith\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#EMAIL jsmith@gmail.com\n",
            "http://somewhere#University http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/FN http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://somewhere#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://somewhere#JaneSmith http://www.w3.org/2001/vcard-rdf/3.0#familyname Smith\n",
            "http://somewhere#SaraJones http://www.w3.org/2001/vcard-rdf/3.0/FN Sara Jones\n",
            "http://somewhere#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "g.add((ns.Jown, FOAF.knows, ns.JaneSmith))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.11.6"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
