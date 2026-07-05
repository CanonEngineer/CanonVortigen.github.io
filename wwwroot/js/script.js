// ==============================
// INICIALIZAÇÃO
// ==============================

document.addEventListener("DOMContentLoaded", () => {
  revealElements();
  animateCounters();
  createBackToTopButton();
  createParticles();
  setupNavbar();
  setupActiveMenu();
});

// ==============================
// ANIMAÇÃO AO ROLAR
// ==============================

function revealElements() {
  const elements = document.querySelectorAll(
    ".card, .timeline-card, .stat-card, .badges span"
  );

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
        }
      });
    },
    {
      threshold: 0.15
    }
  );

  elements.forEach(el => {
    el.style.opacity = "0";
    el.style.transform = "translateY(40px)";
    el.style.transition = "all .8s ease";
    observer.observe(el);
  });
}

// ==============================
// CONTADORES
// ==============================

function animateCounters() {
  const counters = document.querySelectorAll(".stat-card h3");

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;

        const el = entry.target;
        const value = el.innerText;

        if (value.includes("+")) {
          animateNumber(el, parseInt(value), "+");
        }

        if (value === "3") {
          animateNumber(el, 3, "");
        }

        observer.unobserve(el);
      });
    },
    {
      threshold: 0.5
    }
  );

  counters.forEach(counter => observer.observe(counter));
}

function animateNumber(element, target, suffix) {
  let current = 0;

  const increment = target / 40;

  const timer = setInterval(() => {
    current += increment;

    if (current >= target) {
      current = target;
      clearInterval(timer);
    }

    element.innerText =
      Math.floor(current) + suffix;
  }, 35);
}

// ==============================
// NAVBAR SCROLL
// ==============================

function setupNavbar() {
  const navbar = document.querySelector(".navbar");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 80) {
      navbar.style.background =
        "rgba(2,6,23,.97)";
      navbar.style.boxShadow =
        "0 8px 30px rgba(0,0,0,.35)";
    } else {
      navbar.style.background =
        "rgba(2,6,23,.85)";
      navbar.style.boxShadow = "none";
    }
  });
}

// ==============================
// MENU ATIVO
// ==============================

function setupActiveMenu() {
  const sections =
    document.querySelectorAll("section");

  const navLinks =
    document.querySelectorAll(".navbar a");

  window.addEventListener("scroll", () => {
    let current = "";

    sections.forEach(section => {
      const top =
        section.offsetTop - 150;

      if (window.scrollY >= top) {
        current = section.id;
      }
    });

    navLinks.forEach(link => {
      link.classList.remove("active");

      if (
        link.getAttribute("href") ===
        `#${current}`
      ) {
        link.classList.add("active");
      }
    });
  });
}

// ==============================
// BOTÃO VOLTAR AO TOPO
// ==============================

function createBackToTopButton() {
  const button =
    document.createElement("button");

  button.innerHTML =
    '<i class="fas fa-arrow-up"></i>';

  button.id = "backToTop";

  document.body.appendChild(button);

  Object.assign(button.style, {
    position: "fixed",
    right: "30px",
    bottom: "30px",
    width: "55px",
    height: "55px",
    borderRadius: "18px",
    border: "none",
    background: "#2563eb",
    color: "#fff",
    fontSize: "1.1rem",
    cursor: "pointer",
    zIndex: "999",
    opacity: "0",
    visibility: "hidden",
    transition: ".3s"
  });

  window.addEventListener("scroll", () => {
    if (window.scrollY > 500) {
      button.style.opacity = "1";
      button.style.visibility = "visible";
    } else {
      button.style.opacity = "0";
      button.style.visibility = "hidden";
    }
  });

  button.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });
}

// ==============================
// PARTÍCULAS DE FUNDO
// ==============================

function createParticles() {
  const canvas =
    document.createElement("canvas");

  canvas.id = "particles";

  document.body.prepend(canvas);

  Object.assign(canvas.style, {
    position: "fixed",
    top: 0,
    left: 0,
    width: "100%",
    height: "100%",
    zIndex: "-1",
    pointerEvents: "none"
  });

  const ctx =
    canvas.getContext("2d");

  resize();

  window.addEventListener(
    "resize",
    resize
  );

  const particles = [];

  for (let i = 0; i < 70; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 2 + 1,
      dx: (Math.random() - 0.5) * 0.3,
      dy: (Math.random() - 0.5) * 0.3
    });
  }

  function animate() {
    ctx.clearRect(
      0,
      0,
      canvas.width,
      canvas.height
    );

    particles.forEach(p => {
      p.x += p.dx;
      p.y += p.dy;

      if (
        p.x < 0 ||
        p.x > canvas.width
      ) {
        p.dx *= -1;
      }

      if (
        p.y < 0 ||
        p.y > canvas.height
      ) {
        p.dy *= -1;
      }

      ctx.beginPath();
      ctx.arc(
        p.x,
        p.y,
        p.r,
        0,
        Math.PI * 2
      );

      ctx.fillStyle =
        "rgba(96,165,250,.4)";
      ctx.fill();
    });

    requestAnimationFrame(
      animate
    );
  }

  animate();

  function resize() {
    canvas.width =
      window.innerWidth;

    canvas.height =
      window.innerHeight;
  }
}
