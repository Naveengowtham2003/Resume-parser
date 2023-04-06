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
     

document.getElementById("signup").addEventListener("click",function(){
    var email = document.getElementById("email_id").value;
    var password = document.getElementById("password").value;
    var name = document.getElementById("Name").value;
    var username = document.getElementById("username").value;
    var highest_qualification = document.getElementById("highest_qualification").value;
    var company_name = document.getElementById("companyname").value;

    console.log(email);
    console.log(password);

    auth.createUserWithEmailAndPassword(email, password)
    .then(function(){
        var user= auth.currentUser
        var database_ref = database.ref()

        console.log(user);
        
        var user_data = {
            name: name,
            username: username,
            highest_qualification : highest_qualification,
            company_name: company_name,
            last_login : Date.now()
        }

        database_ref.child('users/' + user.uid)
        .set(user_data)
        .then(()=>{
          alert("Signed up Successfully...")
          window.location.assign("applicant_interface.html");
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
