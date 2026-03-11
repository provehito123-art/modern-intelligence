import React, { useState, useEffect } from 'react';
import { Rocket, Target, Zap, Globe, DollarSign, Search, ShieldCheck, Activity, ChevronRight, CheckCircle2, AlertTriangle } from 'lucide-react';

// Custom CSS for the spaceship cursor, starry background, and animations
const globalStyles = `
  body {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="%23a855f7" d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19M5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5M21.61 2.39C21.61 2.39 16.66 .269 11 5.93C8.81 8.12 7.5 10.53 6.65 12.64C6.37 13.39 6.56 14.21 7.11 14.77L9.24 16.89C9.79 17.45 10.61 17.63 11.36 17.35C13.5 16.5 15.88 15.19 18.07 13C23.73 7.34 21.61 2.39 21.61 2.39M14.54 9.46C13.76 8.68 13.76 7.41 14.54 6.63S16.59 5.85 17.37 6.63C18.14 7.41 18.15 8.68 17.37 9.46C16.59 10.24 15.32 10.24 14.54 9.46M8.88 16.53L7.47 15.12L3.59 19L5 20.41L8.88 16.53M16.53 8.88L15.12 7.47L19 3.59L20.41 5L16.53 8.88Z"/></svg>') 0 0, auto;
    background-color: #050014;
    background-image: 
      radial-gradient(at 0% 0%, rgba(67, 24, 114, 0.4) 0px, transparent 50%),
      radial-gradient(at 100% 100%, rgba(31, 10, 51, 0.6) 0px, transparent 50%);
    color: #e2e8f0;
    font-family: 'Inter', -apple-system, sans-serif;
  }
  
  .star {
    position: absolute;
    background: white;
    border-radius: 50%;
    animation: twinkle infinite alternate;
  }
  
  @keyframes twinkle {
    0% { opacity: 0.2; transform: scale(0.8); }
    100% { opacity: 1; transform: scale(1.2); box-shadow: 0 0 8px rgba(255,255,255,0.8); }
  }

  .glass-card {
    background: rgba(20, 10, 40, 0.5);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
  }

  .neon-border:hover {
    border-color: rgba(168, 85, 247, 0.8);
    box-shadow: 0 0 15px rgba(168, 85, 247, 0.4);
  }
  
  .scan-line {
    width: 100%;
    height: 2px;
    background: #a855f7;
    position: absolute;
    top: 0;
    left: 0;
    box-shadow: 0 0 10px #a855f7, 0 0 20px #a855f7;
    animation: scan 2s linear infinite;
    display: none;
  }
  
  .scanning .scan-line {
    display: block;
  }

  @keyframes scan {
    0% { top: 0; opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { top: 100%; opacity: 0; }
  }
`;

// Competitor Data
const competitors = [
  { name: "Foothills Sports Medicine", url: "foothillsrehab.com", strength: "Local SEO Dominance" },
  { name: "Banner Sports Medicine", url: "bannerhealth.com", strength: "Hospital Network Trust" },
  { name: "SOL Physical Therapy", url: "solpt.com", strength: "Pelvic Niche Branding" },
  { name: "Bodycentral PT", url: "bodycentralpt.net", strength: "Aggressive Google Ads" }
];

export default function App() {
  const [isScanning, setIsScanning] = useState(false);
  const [progress, setProgress] = useState(0);
  const [showResults, setShowResults] = useState(false);

  // Generate random stars for the background
  const [stars, setStars] = useState([]);
  useEffect(() => {
    const newStars = Array.from({ length: 50 }).map(() => ({
      left: `${Math.random() * 100}%`,
      top: `${Math.random() * 100}%`,
      size: `${Math.random() * 3 + 1}px`,
      duration: `${Math.random() * 3 + 2}s`,
      delay: `${Math.random() * 2}s`
    }));
    setStars(newStars);
  }, []);

  const handleScan = () => {
    setIsScanning(true);
    setShowResults(false);
    setProgress(0);
    
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval);
          setIsScanning(false);
          setShowResults(true);
          return 100;
        }
        return prev + 2;
      });
    }, 50);
  };

  return (
    <div className="min-h-screen relative overflow-hidden p-6 md:p-10">
      <style>{globalStyles}</style>
      
      {/* Starfield Background */}
      <div className="fixed inset-0 pointer-events-none z-0">
        {stars.map((star, i) => (
          <div 
            key={i} 
            className="star"
            style={{
              left: star.left,
              top: star.top,
              width: star.size,
              height: star.size,
              animationDuration: star.duration,
              animationDelay: star.delay
            }}
          />
        ))}
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        
        {/* Header Section */}
        <header className="mb-12 flex flex-col md:flex-row justify-between items-center gap-6 glass-card p-6 rounded-2xl">
          <div>
            <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-blue-400 tracking-tight flex items-center gap-3">
              <Activity className="w-8 h-8 text-purple-500" />
              Modern Med Intel
            </h1>
            <p className="text-gray-400 mt-2 text-sm uppercase tracking-widest font-semibold">Arizona Competitive Intelligence Matrix</p>
          </div>
          <div className="flex items-center gap-4 bg-black/40 p-3 rounded-xl border border-purple-500/20">
            <span className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
              <span className="text-sm font-medium text-gray-300">Target: getmodernmedicine.com</span>
            </span>
          </div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          
          {/* Left Sidebar: Competitor Targets */}
          <div className="lg:col-span-1 flex flex-col gap-4">
            <div className="glass-card rounded-2xl p-6 h-full border border-purple-500/20">
              <h3 className="text-xl font-bold mb-6 flex items-center gap-2 text-purple-300">
                <Target className="w-5 h-5" /> 
                Monitored Targets
              </h3>
              
              <div className="space-y-4">
                {competitors.map((comp, idx) => (
                  <div key={idx} className="bg-black/40 p-4 rounded-xl border border-white/5 hover:border-purple-500/30 transition-all group">
                    <h4 className="font-semibold text-gray-200 group-hover:text-purple-400 transition-colors">{comp.name}</h4>
                    <p className="text-xs text-gray-500 mt-1">{comp.url}</p>
                    <div className="mt-3 flex items-center gap-1.5 text-xs text-blue-400 bg-blue-900/20 w-fit px-2 py-1 rounded-md">
                      <ShieldCheck className="w-3 h-3" />
                      {comp.strength}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Main Analytics Area */}
          <div className="lg:col-span-3">
            
            {/* Control Panel */}
            <div className="glass-card rounded-2xl p-8 mb-8 text-center border border-purple-500/30 relative overflow-hidden group">
              <div className="absolute inset-0 bg-gradient-to-r from-purple-600/10 to-blue-600/10 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
              
              <h2 className="text-2xl font-bold text-white mb-4">Deep Market Scan</h2>
              <p className="text-gray-400 mb-8 max-w-2xl mx-auto">
                Initiating comprehensive scan of competitor infrastructure, SEO positioning, UI/UX advantages, and pricing strategies against Modern Medicine.
              </p>
              
              <button 
                onClick={handleScan}
                disabled={isScanning}
                className={`relative overflow-hidden px-8 py-4 rounded-full font-bold text-lg transition-all duration-300 transform hover:scale-105 ${
                  isScanning 
                    ? 'bg-purple-900/50 text-purple-300 cursor-not-allowed border border-purple-500/50' 
                    : 'bg-gradient-to-r from-purple-600 to-blue-600 text-white shadow-[0_0_20px_rgba(168,85,247,0.4)] hover:shadow-[0_0_30px_rgba(168,85,247,0.6)]'
                }`}
              >
                {isScanning ? (
                  <span className="flex items-center gap-3">
                    <Rocket className="w-5 h-5 animate-pulse" />
                    Analyzing Data... {progress}%
                  </span>
                ) : (
                  <span className="flex items-center gap-3">
                    <Search className="w-5 h-5" />
                    Launch Deep Analytics
                  </span>
                )}
                
                {/* Progress bar inside button */}
                {isScanning && (
                  <div 
                    className="absolute bottom-0 left-0 h-1 bg-white/50 transition-all duration-75"
                    style={{ width: `${progress}%` }}
                  ></div>
                )}
              </button>
            </div>

            {/* Results Grid */}
            {showResults && (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 animate-[fadeIn_0.5s_ease-out]">
                
                {/* SEO & Content Card */}
                <div className={`glass-card rounded-2xl p-6 border border-purple-500/20 neon-border scanning relative overflow-hidden`}>
                  <div className="scan-line"></div>
                  <div className="flex items-center gap-3 mb-4">
                    <div className="p-3 bg-purple-500/20 rounded-lg text-purple-400">
                      <Globe className="w-6 h-6" />
                    </div>
                    <h3 className="text-xl font-bold text-white">SEO & Content</h3>
                  </div>
                  <div className="space-y-4">
                    <div className="bg-red-900/20 border border-red-500/20 p-3 rounded-xl">
                      <p className="text-sm font-semibold text-red-400 flex items-center gap-2 mb-1"><AlertTriangle className="w-4 h-4"/> Competitor Edge</p>
                      <p className="text-sm text-gray-300"><strong>Foothills</strong> dominates local pack for "Physical Therapy Tucson" due to 120+ referring domains. <strong>SOL PT</strong> ranks #1 for "Pelvic Floor Therapy AZ".</p>
                    </div>
                    <div className="bg-blue-900/20 border border-blue-500/20 p-3 rounded-xl">
                      <p className="text-sm font-semibold text-blue-400 flex items-center gap-2 mb-1"><Target className="w-4 h-4"/> Our Gap</p>
                      <p className="text-sm text-gray-300">Modern Medicine lacks localized schema markup (JSON-LD). The Pelvic Center temp page is not optimized for long-tail keywords like "postpartum therapy Tucson".</p>
                    </div>
                    <div className="bg-green-900/20 border border-green-500/20 p-3 rounded-xl">
                      <p className="text-sm font-semibold text-green-400 flex items-center gap-2 mb-1"><CheckCircle2 className="w-4 h-4"/> Action Plan</p>
                      <ul className="text-sm text-gray-300 space-y-1 list-disc list-inside">
                        <li>Implement Local Business Schema immediately.</li>
                        <li>Create a dedicated "Tucson Postpartum Recovery" long-form article.</li>
                      </ul>
                    </div>
                  </div>
                </div>

                {/* UTP & Offer Card */}
                <div className={`glass-card rounded-2xl p-6 border border-purple-500/20 neon-border scanning relative overflow-hidden`}>
                  <div className="scan-line" style={{animationDelay: "0.5s"}}></div>
                  <div className="flex items-center gap-3 mb-4">
                    <div className="p-3 bg-blue-500/20 rounded-lg text-blue-400">
                      <Zap className="w-6 h-6" />
                    </div>
                    <h3 className="text-xl font-bold text-white">UTP & Offer</h3>
                  </div>
                  <div className="space-y-4">
                    <div className="bg-red-900/20 border border-red-500/20 p-3 rounded-xl">
                      <p className="text-sm font-semibold text-red-400 flex items-center gap-2 mb-1"><AlertTriangle className="w-4 h-4"/> Competitor Edge</p>
                      <p className="text-sm text-gray-300"><strong>Bodycentral</strong> promotes "Free 15-Minute Discovery Visits" as a low-barrier entry. <strong>Banner</strong> leverages sheer hospital network authority.</p>
                    </div>
                    <div className="bg-blue-900/20 border border-blue-500/20 p-3 rounded-xl">
                      <p className="text-sm font-semibold text-blue-400 flex items-center gap-2 mb-1"><Target className="w-4 h-4"/> Our Gap</p>
                      <p className="text-sm text-gray-300">Our website looks clean, but the Unique Selling Proposition (UTP) feels generic. We lack a "hook" or lead magnet for hesitant pelvic floor patients.</p>
                    </div>
                    <div className="bg-green-900/20 border border-
