<?php
// Aqui ficam os dados do seu e-mail e da autoresposta!!!
$assunto = "Quero meu e-book"; //Assunto do e-mail q vai chegar na sua caixa de mensagem
$mail = "email@dominio.com.br"; //E-mail que você gostaria de receber os resultados dos formmail's
$assunto_auto = "$nome, Sua Mensagem Foi Recebida Com Sucesso!";//Assunto da Auto Resposta
$website =  "http://vencendogigantes.josuevalandro.com.br/";//Nome do Website
$url_website = "http://vencendogigantes.josuevalandro.com.br/";//Url do Website
$nome_webmaster = "Pastor Josué Valandro Jr.";//Nome do Webmaster do site
$mensagem_auto = "Obrigado por entrar em contato conosco $nome!\n Ao final da campanha você receberá neste mesmo e-mail o seu ebook!!!\n\n Um abraço! $nome_webmaster";
$assunto_auto = "Recebemos sua mensagem";

// Aqui ficam os dados do formulário que serão enviados!!!
$nome = $_POST["nome"];//Campo Nome do Formulário
$email = $_POST["email"];//Campo E-mail do Formulário
$telefone = $_POST["telefone"];//Campo Contato do Formulário
$mensagem = "Formulário enviado por $nome no Website $website:\n\n";//Inicio da Mensagem enviada! 
$mensagem .= "Nome: $nome\n";//Nome do Contato
$mensagem .= "E-mail: $email\n";//Nome do Contato
$mensagem .= "Telefone: $telefone";//Mensagem Enviada do Contato
//não modifique esta linha, pois é ela que envia a mensagem!!!
@mail($mail, $assunto, $mensagem, "From: $email");
//não modifique esta linha, pois é ela que envia a auto_resposta!!!
@mail($email, $assunto_auto, $mensagem_auto, "From: $mail");
header("Location:ok.php");
?>