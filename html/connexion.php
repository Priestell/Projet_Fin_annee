<?php
    try{
        $pdo = new PDO("mysql:host=192.168.1.105;port=3306;dbname=messagerie;charset=utf8", "malo", "malo");
    }
    catch(PDOException $e){
        print "Erreur !: " . $e->getMessage() . "<br/>";
    }

    $connexion_possible = true;

    if(empty($_POST['email']) or empty($_POST['motdepasse'])){
        echo "Veuillez renseigner votre adresse mail ainsi que votre mot de passe dans les champs prévus à cet effet.<br>";
        $connexion_possible = false;
    }

    $email = $_POST['email'];
    $recherche_email = $pdo -> query("SELECT * FROM utilisateur WHERE Email = '$email'");
    $email_dans_bdd = $recherche_email ->fetch();
    if(!($email_dans_bdd)){
        echo "Aucun compte ne correspond à l'adresse email saisie.<br>";
        $connexion_possible = false;
    }

    $motdepasse = $_POST['motdepasse'];
    $recherche_motdepasse = $pdo -> query("SELECT Motdepasse FROM utilisateur WHERE Email = '$email'");
    $motdepasse_chiffre = $recherche_motdepasse -> fetchColumn();
    if(!(password_verify($motdepasse, $motdepasse_chiffre))){
        echo "Le mot de passe saisi est incorrect.<br>";
        $connexion_possible = false;
    }

    if($connexion_possible)
    {
        session_start();

        $recherche_nom_utilisateur = $pdo -> query("SELECT Nom FROM utilisateur WHERE Email = '$email'");
        $nom_utilisateur = $recherche_nom_utilisateur -> fetchColumn();
        $_SESSION["nomUtilisateur"] = $nom_utilisateur;

        header("messagerie.html");
        exit();
        }
        else{
            header("connexion.html");
            exit();
        }
?>