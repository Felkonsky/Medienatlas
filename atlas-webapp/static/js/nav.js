document.addEventListener('DOMContentLoaded', function() {
    
    let recent_link = null;
    
    const btnToTop = document.querySelector('.btn-to-top');
  
    // Show/hide button-to-top
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        btnToTop.classList.add("visible");
      } else {
        btnToTop.classList.remove("visible");
      }
    });
  
    // Scroll to top 
    btnToTop.addEventListener("click", function(event) {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });

    const headerLinks = document.querySelectorAll(".clickme");
    
    const contentMap = {
        "filter": "<div class='mt-15'><div class='row'><div class='col'><p class='ext-content-heading-red'>Medienarten</p><ul><li>Text</li><li>Bilder</li><li>Audio</li><li>Video</li><li>3D Objekt</li></div><div class='col'><p class='ext-content-heading-green'>Interaktionen</p><ul><li>Vergrößern</li><li>Vergleichen</li><li>Verknüpfen</li><li>Vergrößern</li><li>Fokussieren</li><li>Bewegen</li></div><div class='col'><p class='ext-content-heading-blue'>Visualisierungen</p><ul><li>Buch</li><li>Kacheln</li><li>Karte</li><li>Zeitstrahl</li></ul></div></div></div>",
        'ansicht': '<div class="mt-15"><p>Ansicht content goes here...</p></div>',
        'hilfe': '<div class="mt-15"><p>Hilfe content goes here...</p></div>',
        "suche": '<div class="search-wrapper mt-15"><input id="search" type="text" class="gsearch" autocapitalize="off" autocomplete="off" autocorrect="off" placeholder="Medienatlas durchsuchen..." maxlength="128"><button class="gsearch-btn"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="24" height="24" viewBox="0 0 20 20"><path d="M8.906 14.156c0.729 0 1.411-0.135 2.047-0.406 0.635-0.281 1.193-0.656 1.672-1.125 0.479-0.479 0.854-1.037 1.125-1.672 0.281-0.646 0.422-1.333 0.422-2.062s-0.141-1.411-0.422-2.047c-0.271-0.646-0.646-1.203-1.125-1.672-0.479-0.479-1.037-0.854-1.672-1.125-0.635-0.281-1.318-0.422-2.047-0.422s-1.417 0.141-2.063 0.422c-0.635 0.271-1.193 0.646-1.672 1.125-0.479 0.469-0.859 1.026-1.141 1.672-0.271 0.635-0.406 1.318-0.406 2.047s0.141 1.417 0.422 2.062c0.281 0.635 0.656 1.193 1.125 1.672 0.479 0.469 1.036 0.844 1.672 1.125 0.646 0.271 1.333 0.406 2.063 0.406zM8.906 15.047c-0.854 0-1.656-0.162-2.406-0.484-0.74-0.323-1.391-0.76-1.953-1.313-0.552-0.562-0.99-1.219-1.312-1.969s-0.484-1.547-0.484-2.391c0-0.854 0.161-1.651 0.484-2.391 0.323-0.75 0.76-1.401 1.312-1.953 0.563-0.563 1.214-1.005 1.953-1.328 0.75-0.323 1.552-0.484 2.406-0.484 0.844 0 1.635 0.161 2.375 0.484 0.75 0.323 1.401 0.766 1.953 1.328 0.562 0.552 1.005 1.203 1.328 1.953 0.323 0.74 0.484 1.536 0.484 2.391 0 0.844 0 1.323 0 1.437 0 0.104 0 0.052 0-0.156 0-0.219 0-0.484 0-0.797 0-0.323 0-0.484 0-0.484s0 0.005 0 0.016c0 0.844-0.162 1.641-0.484 2.391s-0.76 1.401-1.313 1.953c-0.552 0.552-1.203 0.99-1.953 1.313s-1.547 0.484-2.391 0.484zM12.984 13.609l3.516 3.516c0.042 0.042 0.088 0.073 0.141 0.094s0.109 0.031 0.172 0.031c0.125 0 0.229-0.042 0.313-0.125s0.125-0.188 0.125-0.313c0-0.063-0.010-0.12-0.031-0.172s-0.052-0.099-0.094-0.141l-3.516-3.516c-0.042-0.042-0.089-0.073-0.141-0.094s-0.109-0.031-0.172-0.031c-0.125 0-0.229 0.042-0.313 0.125s-0.125 0.188-0.125 0.313c0 0.063 0.010 0.12 0.031 0.172s0.052 0.099 0.094 0.141z"></path></svg></button></div>'
    };
    const heightMap = {
        'filter': '189px',
        'ansicht': '49px',
        'hilfe': '49px',
        'suche': '89px'
    };

    const header = document.getElementById("header");
    const extendedHeader = document.getElementById("extended-header");
    const extendedHeaderContent = document.getElementById("extended-header-content");

    headerLinks.forEach(link => {

        link.addEventListener("click", function(event) {

            event.preventDefault();
            
            let contentKey = event.target.getAttribute("data-content");
            extendedHeader.style.height = heightMap[contentKey];

            setTimeout(() => {
                extendedHeaderContent.innerHTML = contentMap[contentKey];
                extendedHeaderContent.classList.add("opaque") 
            }, 100);
            
            if (recent_link) {
                recent_link.classList.remove("active-link");
            }
            
            recent_link = this;
            this.classList.add("active-link");
            header.style.backgroundColor = "white";
        });
    });
    
    document.addEventListener("click", function(event) {
        
        if (!header.contains(event.target) && recent_link) {
            recent_link.classList.remove("active-link");
            extendedHeader.removeAttribute("style");
            header.removeAttribute("style");
            extendedHeaderContent.classList.remove("opaque")
            recent_link = null;
            extendedHeaderContent.innerHTML = "";
        } 
    });
});