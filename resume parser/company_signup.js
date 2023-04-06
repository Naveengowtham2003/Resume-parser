const firebaseConfig = {
    apiKey: "AIzaSyCWYZxcRcK0ohsr465bnUufwLekND1EGPU",
    authDomain: "resume-parser-913c4.firebaseapp.com",
    projectId: "resume-parser-913c4",
    storageBucket: "resume-parser-913c4.appspot.com",
    messagingSenderId: "468299074766",
    appId: "1:468299074766:web:6088d4ec71cb6fe55f549f",
    measurementId: "G-59QNMLQ7XM",
    databaseURL: "https://resume-parser-913c4-default-rtdb.firebaseio.com"

    
  };

  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
  
  const database = firebase.database();
  const auth = firebase.auth();
     

document.getElementById("company_signup").addEventListener("click",function(){
    var email = document.getElementById("email_id").value;
    var password = document.getElementById("password").value;
    var name_of_the_companyholder = document.getElementById("namecomholder").value;
    var company_id = document.getElementById("Companyid").value;
    var name_of_the_company = document.getElementById("namecompany").value;
    var username = document.getElementById("usernamecom").value;
  
    console.log(email);
    console.log(password);
  
    auth.createUserWithEmailAndPassword(email, password)
    .then(function(){
        var user = auth.currentUser
        var database_ref = database.ref()
        console.log(user);
        
        
        
        var user_data = {
          name_of_the_companyholder: name_of_the_companyholder,
          username: username,
          company_id : company_id,
          name_of_the_company : name_of_the_company,
          last_login : Date.now()
        }
  
        database_ref.child('company/' + user.uid)
        .set(user_data)
        .then(()=>{
          alert("Signed up Successfully...")
          window.location.assign("company_interface.html");
        })
        .catch((err)=>{
          alert("Data add failed")
        })
      
    })
  
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      console.log(error);
      alert(error);
    });
    
  
  });
