<html>
<head>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<!-- Attach stylesheet-->
<link rel="stylesheet" href="style.css">

</head>


<body>


    <div id="graph-container"></div>

    <div id="searchPane">
      <div id='header'> <h2>Search Bar</h2> </div>

      <form>

      <label for="lastName">Last name:</label><br><br>
      <input type="text" id="lastName" name="lastName" value="Any"/><br><br>

      <label for="pubTitle">Title Keyword:</label><br><br>
      <input type="text" id="pubTitle" name="pubTitle" value="Any"/><br><br>

      <label for="pubField">Field:</label><br><br>
      <select id="pubField" name="pubField" multiple>
        <option value="Computer Science" selected>Computer Science</option>

      </select><br><br>


      <label for="pubType">Type:</label><br><br>
      <select id="pubType" name="pubType" multiple>
        <option value="Article" selected>Article</option>
      </select><br><br>

      <label for="searchLimit">Max Nodes:</label><br><br>
      <input type="number" id="searchLimit" name="searchLimit" required value="5000" min="1" max="5000"/><br><br>


      <button type="submit" onclick="formChanged(); return false;">Submit</button><br>
      </form>

    </div>


    <div id="control-pane">

    <div id='information' class="close"><div id='limiter'>Sidebar</div></div>
    </div>


<script>


  function formChanged(){

    // Clear div content
    document.getElementById("graph-container").innerHTML = "";


    // Run python script

   $(function()
     {console.log("Starting");
         $.ajax({
             url: "../../cgi-bin/queries.cgi",
             type: "post",
             datatype: "text",
             data: {},
             success: function(response){
                     console.log("Completed");
             }
         });
     });
    return
  }

</script>

</body>
</html>
