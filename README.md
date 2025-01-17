# GET_CONTAINER_IP

[![Alert](https://sonar.koentlab.com/api/project_badges/measure?project=Koent-it_get_container_ip_AZR0w1AuWa--ZuEf7b-8&metric=alert_status&token=sqb_89be40e01f509075033f14a7ab9300a056c3bade)](https://sonar.koentlab.com/dashboard?id=Koent-it_get_container_ip_AZR0w1AuWa--ZuEf7b-8) [![Maintainability Rating](https://sonar.koentlab.com/api/project_badges/measure?project=Koent-it_get_container_ip_AZR0w1AuWa--ZuEf7b-8&metric=sqale_rating&token=sqb_89be40e01f509075033f14a7ab9300a056c3bade)](https://sonar.koentlab.com/dashboard?id=Koent-it_get_container_ip_AZR0w1AuWa--ZuEf7b-8) [![Alert](https://sonar.koentlab.com/api/project_badges/measure?project=Koent-it_get_container_ip_AZR0w1AuWa--ZuEf7b-8&metric=alert_status&token=sqb_89be40e01f509075033f14a7ab9300a056c3bade)](https://sonar.koentlab.com/dashboard?id=Koent-it_get_container_ip_AZR0w1AuWa--ZuEf7b-8)

#

# A simple library and CLI command that provides the IP address of any running docker container.

## TIPICAL USE CASE
You run on a test server some applications that connects to a db that is dockerized. everytime you run the container, you must inspect it to get the IP address and update the connection parameter.

# get_container_ip

Questo pacchetto Python fornisce funzioni per ottenere l'indirizzo IP di un container Docker. È progettato per semplificare l'interazione con i container e facilitare la gestione delle reti.

## Installazione

Per installare il pacchetto, puoi utilizzare pip:

```
pip install get_container_ip
```

## Utilizzo

Ecco un esempio di come utilizzare il pacchetto:

```python
from get_container_ip import main

# Ottieni l'indirizzo IP di un container specifico
ip_address = main.get_container_ip('nome_del_container')
print(f"L'indirizzo IP del container è: {ip_address}")
```

## Contribuire

Se desideri contribuire a questo progetto, sentiti libero di aprire una pull request o segnalare problemi.

## Licenza

Questo progetto è concesso in licenza sotto la MIT License. Vedi il file LICENSE per ulteriori dettagli.