/* ==========================================
   SCRIPT PRINCIPAL - PORTFÓLIO
========================================== */

/* Smooth scroll para links do menu */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    });
});

/* ==========================================
   BOTÃO VOLTAR AO TOPO
========================================== */

const backToTop = document.createElement("button");
backToTop.innerHTML = "↑";
backToTop.classList.add("back-to-top");
document.body.appendChild(backToTop);

window.addEventListener("scroll", () => {
    if (window.scrollY > 500) {
        backToTop.classList.add("show");
    } else {
        backToTop.classList.remove("show");
    }
});

backToTop.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

/* ==========================================
   ANIMAÇÃO AO SCROLL (REVEAL)
========================================== */

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
}, {
    threshold: 0.15
});

document.querySelectorAll(".card, .timeline-card, .stat-card, section h2")
    .forEach(el => {
        el.classList.add("hidden");
        observer.observe(el);
    });

/* ==========================================
   ESTILO DINÂMICO DE ANIMAÇÃO
========================================== */

const style = document.createElement("style");

style.innerHTML = `
.hidden {
    opacity: 0;
    transform: translateY(40px);
    transition: all 0.8s ease;
}

.show {
    opacity: 1;
    transform: translateY(0);
}
`;

document.head.appendChild(style);

/* ==========================================
   NAVBAR SCROLL EFFECT
========================================== */

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
        navbar.style.background = "rgba(2, 6, 23, 0.95)";
        navbar.style.boxShadow = "0 10px 30px rgba(0,0,0,.4)";
    } else {
        navbar.style.background = "rgba(2, 6, 23, 0.75)";
        navbar.style.boxShadow = "none";
    }
});

/* ==========================================
   DIGITAÇÃO (EFEITO HERO)
========================================== */

const title = document.querySelector(".hero h2");

if (title) {
    const text = title.textContent;
    title.textContent = "";

    let i = 0;

    function typeEffect() {
        if (i < text.length) {
            title.textContent += text.charAt(i);
            i++;
            setTimeout(typeEffect, 60);
        }
    }

    typeEffect();
}

/* ==========================================
   CONSOLE BRAND
========================================== */

console.log("%cAlessandro Canon Portfolio Loaded",
    "color:#2563eb;font-size:14px;font-weight:bold;");

const toggle = document.getElementById("themeToggle");

toggle.addEventListener("click", () => {
    document.body.classList.toggle("light");

    toggle.textContent =
        document.body.classList.contains("light")
            ? "☀️"
            : "🌙";
});

window.addEventListener("load", () => {
    const loader = document.getElementById("loader");
    loader.style.opacity = "0";

    setTimeout(() => loader.remove(), 600);
});

const counters = document.querySelectorAll(".stat-card h3");

counters.forEach(counter => {
    const update = () => {
        const target = +counter.innerText.replace("+", "");
        let count = +counter.innerText.replace("+", "");

        if (count < target) {
            counter.innerText = (count + 1) + "+";
            setTimeout(update, 30);
        }
    };

    update();
});

fetch("https://api.countapi.xyz/hit/canon-portfolio/visits")
  .then(res => res.json())
  .then(data => {
      console.log("Visitas:", data.value);
  });

const modal = document.getElementById("modal");
const modalBody = document.getElementById("modalBody");
const closeModal = document.getElementById("closeModal");

document.querySelectorAll("#projetos .card").forEach(card => {
    card.addEventListener("click", () => {
        modal.style.display = "flex";
        modalBody.innerHTML = card.innerHTML;
    });
});

closeModal.onclick = () => {
    modal.style.display = "none";
};

window.onclick = (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
};

/* ==========================================
   BLOG DINÂMICO (MEDIUM STYLE)
========================================== */

document.querySelectorAll(".blog-post").forEach(post => {
    post.addEventListener("click", () => {

        const title = post.getAttribute("data-title");
        const content = post.getAttribute("data-content");

        document.getElementById("modalBody").innerHTML = `
            <h2 style="margin-bottom:15px;color:#2563eb;">${title}</h2>
            <p style="line-height:1.8;color:#cbd5e1;">${content}</p>
        `;

        document.getElementById("modal").style.display = "flex";
    });
});
