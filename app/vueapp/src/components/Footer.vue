<template>
  <div class="footer">
      <div class="hr"></div>

      <div class="footlinks">
          <ul>
              <li><a href="mailto:kyle.koivukangas@gmail.com" ><icon class="ico" name="envelope" scale="1" label="Email"></icon> Email</a></li>
              <li><a target="_blank" href="https://api.whatsapp.com/send?phone=14036808077" ><icon class="ico" name="whatsapp" scale="1" label="whatsapp"></icon> Whatsapp</a></li>
              <li><a target="_blank" href="https://github.com/Kyle-Koivukangas" ><icon class="ico" name="github" scale="1" label="github"></icon> Github</a></li>
              <li><a href="" ><icon class="ico" name="stack-overflow" scale="1" label="stack overflow"></icon> Stack Overflow</a></li>
              <li><a target="_blank" href="https://www.linkedin.com/in/kyle-koivukangas" ><icon class="ico" name="linkedin-square" scale="1" label="linkedin"></icon> LinkedIn</a></li>
          </ul>
      </div>
      
  </div>
</template>

<script>
import "vue-awesome/icons/envelope";
import "vue-awesome/icons/github";
import "vue-awesome/icons/linkedin-square";
import "vue-awesome/icons/stack-overflow";
import "vue-awesome/icons/whatsapp";

export default {};
</script>

<style lang="scss" scoped>
// @import url("https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css");


$contentwidth: 900px;
.footer {
    width: $contentwidth;
    margin: 50px auto;
}
.hr {
    background-color: $lightgrey;
    opacity: 0.6;
    height: 2px;
    width: 100%;
    border-radius: 3px;
}
.footlinks {
    //   display: grid;
    width: 60%;
    margin: 30px auto;
    & ul {
        columns: 3;
        margin: 0 auto;
        text-align: center;
    }
    & li {
        display: inline-block;
        vertical-align: top;
        width: 150px;
        min-height: 30px;
        margin: 5px;
        & a {
            color: $darkgrey;
            text-decoration: none;

            &:hover {
                color: darken($darkgrey, 20%);
                -webkit-animation: pulse 1s;
                animation: pulse 1s;
            }
            & .ico:hover {
                -webkit-animation: pulse 1s;
                animation: pulse 1s;
            }
        }
    }
}
.ico {
    margin: auto;
    display: inline-block;
    & :hover {
        // -webkit-animation: fade 1s;
        // animation: fade 1s;
        // -webkit-animation: pulse 1s;
        // animation: pulse 1s;
    }
}


</style>
