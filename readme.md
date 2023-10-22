#Projeto de medição de temperatura e umidade usando o raspberry pi e o sensor DHT11

#Estrutura do projeto
```mermaid 
graph LR
  subgraph Nível Raiz
    data[Data]
    web[Web]
    backend[Backend]
  end

  subgraph Backend
    dht11.py[dht11.py]
  end

  subgraph Data
    sensor_quarto.db[sensor_quarto.db]
  end

  subgraph Web
    webserver-sensor.py[webserver-sensor.py]
    dockerfile[Dockerfile]
    requiriments.txt[requiriments.txt]
    templates[templates]
  end

  subgraph Templates
    index.html[index.html]
  end

  data --> sensor_quarto.db
  web --> webserver-sensor.py
  web --> dockerfile
  web --> requiriments.txt
  web --> templates
  backend --> dht11.py
```
