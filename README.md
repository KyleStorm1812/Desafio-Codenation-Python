# Desafio-Codenation-Python
Repository for the pre-registration phase of the Python AceleraDev Program, by Codenation.

The purpose of this code is to utilize a GET method to make an HTTP request, retrieve a .json file with a crypted message,
decrypt it and post it back to the proper API.

The result must return the score of this phase:

![photo_2020-05-02_19-58-05](https://user-images.githubusercontent.com/49794037/80894296-21f41b00-8cb0-11ea-9be5-02988453f576.jpg)


# Criptografia de Júlio César
Segundo o Wikipedia, criptografia ou criptologia (em grego: kryptós, “escondido”, e gráphein, “escrita”) é o estudo e prática de princípios e técnicas para comunicação segura na presença de terceiros, chamados “adversários”. Mas geralmente, a criptografia refere-se à construção e análise de protocolos que impedem terceiros, ou o público, de lerem mensagens privadas. Muitos aspectos em segurança da informação, como confidencialidade, integridade de dados, autenticação e não-repúdio são centrais à criptografia moderna. Aplicações de criptografia incluem comércio eletrônico, cartões de pagamento baseados em chip, moedas digitais, senhas de computadores e comunicações militares. Das Criptografias mais curiosas na história da humanidade podemos citar a criptografia utilizada pelo grande líder militar romano Júlio César para comunicar com os seus generais. Essa criptografia se baseia na substituição da letra do alfabeto avançado um determinado número de casas. Por exemplo, considerando o número de casas = 3:

**Normal**: a ligeira raposa marrom saltou sobre o cachorro cansado

**Cifrado**: d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr

# Regras
- As mensagens serão convertidas para minúsculas tanto para a criptografia quanto para descriptografia.
- No nosso caso os números e pontos serão mantidos, ou seja:

**Normal**: 1a.a

**Cifrado**: 1d.d

Escrever programa, em qualquer linguagem de programação, que faça uma requisição HTTP para a url abaixo:

``` 
https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN 
```
Para encontrar o seu token , acesse a plataforma Codenation, faça o login e a informação estará na tela.

O resultado da requisição vai ser um arquivo .json. O primeiro passo é você salvar o conteúdo do .json em um arquivo com o nome answer.json, que irá usar no restante do desafio.

Você deve usar o número de casas para decifrar o texto e atualizar o arquivo .json, no campo decifrado. O próximo passo é gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1 e atualizar novamente o arquivo .json. 
OBS: você pode usar qualquer biblioteca de criptografia da sua linguagem de programação favorita para gerar o resumo sha1 do texto decifrado.

Seu programa deve submeter o arquivo atualizado para correção via POST para a API: 

``` 
https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN 
```
OBS: a API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML, com um campo do tipo file com o nome answer. Considere isso ao enviar o arquivo.

O resultado da submissão vai ser sua nota ou o erro correspondente. Você pode submeter quantas vezes achar necessário, mas a API não vai permitir mais de uma submissão por minuto.
